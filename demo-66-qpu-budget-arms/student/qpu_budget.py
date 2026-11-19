"""Demo 66 teaching toy: three workflow arms spend one simulated QPU budget.

Every number here is synthetic. The device, the instances and their reference values
are hand-built fixtures; no quantum hardware, simulator library or language model is
called. The noise model is a deliberately simple global-depolarising approximation:

    noisy expectation = ideal expectation * (1 - p2) ** two_qubit_gates * (1 - 2 * readout)

Zero-noise extrapolation (ZNE) is modelled as a two-point Richardson extrapolation at
noise scale factors 1 and 3, which costs three times the shots of the scale-1 run on top
of the scale-1 run itself (gate folding triples circuit depth at scale 3).
"""
from __future__ import annotations

import math
import random

SCALES = (1, 3)


def attenuation(instance: dict, device: dict, scale: int = 1) -> float:
    """Multiplicative signal loss for one circuit at a noise scale factor."""
    gate = (1.0 - device["two_qubit_error"]) ** (instance["two_qubit_gates"] * scale)
    readout = 1.0 - 2.0 * device["readout_error"]
    return gate * readout


def fits_device(instance: dict, device: dict, scale: int = 1) -> bool:
    return instance["depth"] * scale <= device["max_depth"] and instance["qubits"] <= device["qubits"]


def job_seconds(shots: int, device: dict) -> float:
    """Simulated QPU seconds charged for one job (fixed overhead plus per-shot time)."""
    return device["job_overhead_s"] + shots * device["shot_time_s"]


def run_job(instance: dict, device: dict, shots: int, scale: int, rng: random.Random) -> dict:
    """One simulated job. A job that does not fit the device fails but is still charged."""
    seconds = job_seconds(shots, device)
    if not fits_device(instance, device, scale):
        return {"ok": False, "seconds": seconds, "estimate": None}
    mean = instance["reference"] * attenuation(instance, device, scale)
    sd = 1.0 / math.sqrt(shots)
    return {"ok": True, "seconds": seconds, "estimate": mean + rng.gauss(0.0, sd)}


def zne(e1: float, e3: float) -> float:
    """Richardson extrapolation to scale 0 from scales 1 and 3 (linear in scale)."""
    return e1 - (e3 - e1) / 2.0


def accepted(estimate: float | None, reference: float, tolerance: float) -> bool:
    return estimate is not None and abs(estimate - reference) <= tolerance


def plan_b0(instance: dict, device: dict, policy: dict) -> dict:
    """B0, provider default: submit every job once, no mitigation."""
    return {"submit": True, "mitigate": False, "shots": policy["shots"]}


def plan_b1(instance: dict, device: dict, policy: dict) -> dict:
    """B1, rule-based and calibration-aware: skip jobs that cannot fit or whose predicted
    attenuation is below a fixed floor; mitigate every job it submits."""
    if not fits_device(instance, device, 3):
        return {"submit": False, "mitigate": False, "shots": 0}
    if attenuation(instance, device, 1) < policy["b1_attenuation_floor"]:
        return {"submit": False, "mitigate": False, "shots": 0}
    return {"submit": True, "mitigate": True, "shots": policy["shots"]}


def predicted_error(instance: dict, device: dict, shots: int, mitigate: bool) -> float:
    """Classical prediction of the absolute error of the returned estimate.

    Without mitigation the error is the attenuation bias plus two shot-noise standard
    deviations. With ZNE the bias left by a linear extrapolation of an exponential decay
    is used, and the shot noise of the extrapolated value is amplified."""
    ref = abs(instance["reference"])
    a1 = attenuation(instance, device, 1)
    sd = 1.0 / math.sqrt(max(shots, 1))
    if not mitigate:
        return ref * (1.0 - a1) + 2.0 * sd
    a3 = attenuation(instance, device, 3)
    residual = ref * abs(1.0 - (a1 - (a3 - a1) / 2.0))
    amplified = sd * math.sqrt(1.5 ** 2 + 0.5 ** 2)
    return residual + 2.0 * amplified


def plan_simulate_first(instance: dict, device: dict, policy: dict) -> dict:
    """Stand-in for the agent arm (A2): simulate first, then decide.

    In the real pilot an open-weight model makes this decision from the same inputs.
    This deterministic stand-in only shows the decision the arm is meant to make: submit
    only when the classical prediction says the result will be accepted, choosing the
    cheapest option (unmitigated, then mitigated) that meets the tolerance."""
    tol = instance["tolerance"]
    for mitigate in (False, True):
        scales = SCALES if mitigate else (1,)
        if not all(fits_device(instance, device, s) for s in scales):
            continue
        if predicted_error(instance, device, policy["shots"], mitigate) <= tol:
            return {"submit": True, "mitigate": mitigate, "shots": policy["shots"]}
    return {"submit": False, "mitigate": False, "shots": 0}


ARMS = {"B0": plan_b0, "B1": plan_b1, "A2-stand-in": plan_simulate_first}


def run_arm(name: str, instances: list, device: dict, policy: dict, seed: int) -> dict:
    """Spend at most the budget on the instances in fixture order."""
    plan = ARMS[name]
    rng = random.Random(seed)
    budget = policy["budget_s"]
    spent = 0.0
    rows = []
    for inst in instances:
        decision = plan(inst, device, policy)
        row = {"instance": inst["id"], "submitted": decision["submit"], "mitigated": decision["mitigate"],
               "seconds": 0.0, "estimate": None, "accepted": False, "failed": False}
        if decision["submit"]:
            shots = decision["shots"]
            scales = SCALES if decision["mitigate"] else (1,)
            cost = sum(job_seconds(shots * s, device) for s in scales)
            if spent + cost > budget:
                row["submitted"] = False
                row["note"] = "budget exhausted"
                rows.append(row)
                continue
            jobs = [run_job(inst, device, shots * s, s, rng) for s in scales]
            spent += cost
            row["seconds"] = round(cost, 6)
            if all(j["ok"] for j in jobs):
                est = jobs[0]["estimate"] if len(jobs) == 1 else zne(jobs[0]["estimate"], jobs[1]["estimate"])
                row["estimate"] = round(est, 6)
                row["accepted"] = accepted(est, inst["reference"], inst["tolerance"])
            else:
                row["failed"] = True
        rows.append(row)
    n_acc = sum(r["accepted"] for r in rows)
    lost = sum(r["seconds"] for r in rows if r["failed"] or (r["submitted"] and not r["accepted"]))
    return {"arm": name, "seconds_spent": round(spent, 6), "accepted": n_acc,
            "accepted_per_qpu_second": round(n_acc / spent, 6) if spent else 0.0,
            "seconds_lost": round(lost, 6), "rows": rows}
