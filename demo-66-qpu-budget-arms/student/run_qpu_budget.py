"""Run the Demo-66 toy: three arms spend one simulated QPU-second budget."""

import json
from pathlib import Path
from qpu_budget import ARMS, run_arm

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def main():
    data = json.loads((ROOT / "fixtures" / "battery.json").read_text())
    device, policy, instances = data["device"], data["policy"], data["instances"]
    results = {}
    print(f"synthetic device {device['name']}; budget {policy['budget_s']} simulated QPU-seconds; {len(instances)} instances")
    for name in ARMS:
        res = run_arm(name, instances, device, policy, policy["seed"])
        results[name] = res
        print(f"{name:<12} spent {res['seconds_spent']:7.2f} s  accepted {res['accepted']}  "
              f"accepted/QPU-s {res['accepted_per_qpu_second']:.4f}  lost {res['seconds_lost']:6.2f} s")
    out = ROOT / "results" / "qpu_budget.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"label": "synthetic teaching output, not evidence", "arms": results}, indent=2) + "\n")
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
