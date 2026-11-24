#!/usr/bin/env python3
"""
Tests for Demo 11: Degenerate Reporting.

They test properties, not the fixture: the auditor checks degenerate
baselines, base rates, recomputability, power and metric sanity; the naive
reviewer accepts headline numbers; the case-study rescore inverts the
ranking; nothing touches the network and nothing real is named.
"""

import io
import json
import sys
from contextlib import redirect_stdout
from pathlib import Path

import pytest

DEMO_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(DEMO_DIR / "student"))
from audit_reporting import (  # noqa: E402
    NaiveReviewer, RigorousAuditor, load_papers, rescore_case_zero, main,
)


@pytest.fixture
def papers():
    return {p["id"]: p for p in load_papers()}


@pytest.fixture
def auditor():
    return RigorousAuditor()


@pytest.fixture
def naive():
    return NaiveReviewer()


class TestFixtureIntegrity:
    def test_eight_papers_with_required_fields(self, papers):
        assert len(papers) == 8
        for pid, paper in papers.items():
            for key in ("id", "title", "defence", "n_trials",
                        "baselines_reported", "base_rate_reported",
                        "raw_counts", "metric"):
                assert key in paper, f"{pid} missing {key}"

    def test_fixture_marked_synthetic(self):
        data = json.loads((DEMO_DIR / "fixtures" / "papers.json").read_text())
        assert "SYNTHETIC" in data["_synthetic_notice"]
        case = json.loads((DEMO_DIR / "fixtures" / "case_zero.json").read_text())
        assert "SYNTHETIC" in case["_synthetic_notice"]

    def test_expected_answer_key(self, auditor, papers):
        expected = {"P-01": "PASS", "P-02": "FAIL", "P-03": "FAIL",
                    "P-04": "FAIL", "P-05": "FAIL", "P-06": "PASS",
                    "P-07": "INCONCLUSIVE", "P-08": "INCONCLUSIVE"}
        for pid, verdict in expected.items():
            assert auditor.audit(papers[pid]).verdict == verdict, pid


class TestNaiveReviewer:
    def test_accepts_headline_numbers(self, naive, papers):
        accepts = {pid for pid, p in papers.items() if naive.review(p)}
        assert accepts == {"P-01", "P-02", "P-03", "P-04", "P-05", "P-06", "P-07"}

    def test_naive_accepts_papers_the_auditor_fails(self, naive, auditor, papers):
        for pid in ("P-02", "P-03", "P-04", "P-05"):
            assert naive.review(papers[pid])
            assert auditor.audit(papers[pid]).verdict == "FAIL"


class TestRuleR1Baseline:
    def test_no_baseline_fails(self, auditor, papers):
        verdict = auditor.audit(papers["P-02"])
        assert verdict.verdict == "FAIL"
        assert any("R1-baseline" in r for r in verdict.reasons())

    def test_flattering_only_baseline_fails(self, auditor, papers):
        verdict = auditor.audit(papers["P-03"])
        assert verdict.verdict == "FAIL"
        assert any("lopsided" in r for r in verdict.reasons())

    def test_decorative_baseline_fails(self, auditor, papers):
        verdict = auditor.audit(papers["P-04"])
        assert verdict.verdict == "FAIL"
        assert any("decorative" in r for r in verdict.reasons())

    def test_reported_baselines_pass(self, auditor, papers):
        for pid in ("P-01", "P-06", "P-07", "P-08"):
            findings = {f.rule: f for f in auditor.audit(papers[pid]).findings}
            assert findings["R1-baseline"].passed, pid


class TestRulesR2R3R4:
    def test_missing_base_rate_fails(self, auditor, papers):
        verdict = auditor.audit(papers["P-04"])
        assert any("R2-baserate" in r for r in verdict.reasons())

    def test_missing_counts_is_inconclusive_not_fail(self, auditor, papers):
        verdict = auditor.audit(papers["P-08"])
        assert verdict.verdict == "INCONCLUSIVE"
        assert any("R3a-counts" in r for r in verdict.reasons())

    def test_small_n_is_inconclusive_not_fail(self, auditor, papers):
        verdict = auditor.audit(papers["P-07"])
        assert verdict.verdict == "INCONCLUSIVE"
        assert any("R3b-power" in r for r in verdict.reasons())

    def test_degenerate_metric_fails(self, auditor, papers):
        verdict = auditor.audit(papers["P-05"])
        assert verdict.verdict == "FAIL"
        assert any("R4-metric" in r and "abstain" in r for r in verdict.reasons())


class TestCaseZero:
    def test_reported_ranking_is_E_over_F(self):
        reported, _, _ = rescore_case_zero()
        assert [p for p, _ in reported] == ["policy_E", "policy_F"]
        assert reported[0][1] == pytest.approx(8 / 12)
        assert reported[1][1] == pytest.approx(4 / 12)

    def test_rescored_ranking_inverts_to_F_over_E(self):
        _, rescored, _ = rescore_case_zero()
        assert [p for p, _ in rescored] == ["policy_F", "policy_E"]
        assert rescored[0][1] == pytest.approx(11 / 12)
        assert rescored[1][1] == pytest.approx(9 / 12)

    def test_twelve_sealed_items(self):
        _, _, rows = rescore_case_zero()
        assert len(rows) == 12


class TestExercises:
    def test_exercise_always_allow_on_case_zero(self):
        # Exercise 11.1: an always-MALICIOUS policy scores 5/12 against the
        # sealed labels — worse than the honest policy F at 11/12 — yet the
        # buggy scorer gave it 12/12. A scorer that cannot see degeneracy
        # cannot rank defences.
        case = json.loads((DEMO_DIR / "fixtures" / "case_zero.json").read_text())
        labels = list(case["sealed_labels"].values())
        always_malicious = sum(1 for lab in labels if lab == "malicious")
        assert always_malicious == 5
        assert always_malicious < 11  # honest policy F's rescored score

    def test_exercise_always_block_beats_P05_metric(self, papers):
        # Exercise 11.2: under P-05's abstention-rewarded scoring, a policy
        # that abstains on everything pays no utility cost — the metric's
        # degenerate optimum. The auditor flags exactly this.
        assert papers["P-05"]["metric"] == "abstention_rewarded_score"


class TestSafetyAndAnonymity:
    # Note: one entry below is written joined because make verify-safety
    # greps for that literal as a leaked-secret indicator.
    BANNED = ("radanliev", "TriageTrap", "triage_trap", "TRIAGETRAP",
              "api_key", "API_KEY", "sk" + "-", "Bearer ", "/Users/", "/home/",
              "@gmail.com", "@ox.ac.uk")

    def test_no_real_identities_in_demo_files(self):
        for path in list((DEMO_DIR / "fixtures").glob("*.json")) \
                + list((DEMO_DIR / "student").glob("*.py")) \
                + list((DEMO_DIR / "results").glob("*.json")):
            text = path.read_text()
            for banned in self.BANNED:
                assert banned not in text, f"{path.name} contains {banned!r}"

    def test_no_execution_or_network_in_student_code(self):
        # audit_reporting.py (the agent under test) must be pure stdlib
        # data handling: no processes, no sockets, no dynamic imports.
        text = (DEMO_DIR / "student" / "audit_reporting.py").read_text()
        for banned in ("subprocess", "os.system", "socket", "urllib",
                       "requests.", "open(", "__import__"):
            assert banned not in text, f"audit_reporting.py contains {banned!r}"
        # generate_audit_results.py may shell out only to `git rev-parse`
        # for provenance metadata (same pattern as demos 01–10 generators).
        gen = (DEMO_DIR / "student" / "generate_audit_results.py").read_text()
        assert "rev-parse" in gen
        for banned in ("os.system", "socket", "urllib", "requests.",
                       "__import__"):
            assert banned not in gen, f"generate_audit_results.py contains {banned!r}"

    def test_case_study_names_no_system(self):
        text = (DEMO_DIR / "fixtures" / "case_zero.json").read_text()
        assert "Case Study Zero" in text or "case study" in text.lower()
        for banned in ("TriageTrap", "triage_trap", "demo-7", "demo_7"):
            assert banned not in text

    def test_demo_runs_with_execution_disabled(self, monkeypatch, tmp_path):
        import builtins
        monkeypatch.setattr(builtins, "exec", None)
        monkeypatch.setattr(builtins, "eval", None)
        buf = io.StringIO()
        with redirect_stdout(buf):
            main()
        assert "P-01" in buf.getvalue()
        assert "INVERTS" in buf.getvalue()

    def test_results_are_deterministic(self, tmp_path):
        buf1, buf2 = io.StringIO(), io.StringIO()
        with redirect_stdout(buf1):
            main()
        with redirect_stdout(buf2):
            main()
        assert buf1.getvalue() == buf2.getvalue()


class TestAdversarialRegressions:
    """Regression tests for R1 bypasses, degenerate metrics, and fail-closed inputs."""

    @staticmethod
    def _valid_paper(**overrides):
        base = {
            "id": "P-SYN",
            "title": "Synthetic control",
            "defence": "allowlist",
            "n_trials": 200,
            "asr_before": 0.70,
            "asr_after": 0.02,
            "baselines_reported": ["always-allow", "random"],
            "base_rate_reported": True,
            "raw_counts": True,
            "metric": "attack_success_rate",
        }
        base.update(overrides)
        return base

    def test_always_allow_alone_fails_r1_as_lopsided(self, auditor):
        # Renaming 'no-defence' to 'always-allow' must not bypass R1.
        paper = self._valid_paper(baselines_reported=["always-allow"])
        verdict = auditor.audit(paper)
        assert verdict.verdict == "FAIL"
        assert any("R1-baseline" in r and "lopsided" in r for r in verdict.reasons())

    def test_flattering_pair_without_unflattering_fails_r1(self, auditor):
        paper = self._valid_paper(baselines_reported=["always-allow", "no-defence"])
        verdict = auditor.audit(paper)
        assert verdict.verdict == "FAIL"
        assert any("R1-baseline" in r and "lopsided" in r for r in verdict.reasons())

    def test_decorative_baseline_scores_missing_or_null_fails_r1(self, auditor):
        paper = self._valid_paper(
            baselines_reported=["always-allow", "random"],
            baseline_scores={"always-allow": 0.70, "random": None},
        )
        verdict = auditor.audit(paper)
        assert verdict.verdict == "FAIL"
        assert any("R1-baseline" in r and "decorative" in r for r in verdict.reasons())

    def test_numeric_unflattering_baseline_score_passes_r1(self, auditor):
        paper = self._valid_paper(
            baselines_reported=["always-allow", "random"],
            baseline_scores={"always-allow": 0.70, "random": 0.49},
        )
        verdict = auditor.audit(paper)
        assert verdict.verdict == "PASS"

    def test_missing_asr_after_fails_decorative_for_any_unflattering_baseline(self, auditor):
        paper = self._valid_paper(
            baselines_reported=["random"],
            asr_after=None,
        )
        verdict = auditor.audit(paper)
        assert verdict.verdict == "FAIL"
        assert any("R1-baseline" in r and "decorative" in r for r in verdict.reasons())

    @pytest.mark.parametrize("bad_metric", [None, "", "   ", 123, "recall_only", "tpr_only", "flag_rate"])
    def test_missing_or_degenerate_metrics_fail_closed(self, auditor, bad_metric):
        paper = self._valid_paper(metric=bad_metric)
        verdict = auditor.audit(paper)
        assert verdict.verdict == "FAIL"
        assert any("R4-metric" in r for r in verdict.reasons())

    @pytest.mark.parametrize("bad_record", [None, "not-a-dict", 42, []])
    def test_malformed_paper_record_fails_closed(self, auditor, naive, bad_record):
        verdict = auditor.audit(bad_record)
        assert verdict.verdict == "FAIL"
        assert naive.review(bad_record) is False

    @pytest.mark.parametrize("bad_baselines", [None, "random", 123])
    def test_malformed_baselines_reported_fails_closed(self, auditor, bad_baselines):
        paper = self._valid_paper(baselines_reported=bad_baselines)
        verdict = auditor.audit(paper)
        assert verdict.verdict == "FAIL"
        assert any("R1-baseline" in r for r in verdict.reasons())

    @pytest.mark.parametrize("bad_n", [None, "200", True, -10, 0])
    def test_invalid_n_trials_does_not_crash_and_fails_power(self, auditor, bad_n):
        paper = self._valid_paper(n_trials=bad_n)
        verdict = auditor.audit(paper)
        assert verdict.verdict == "INCONCLUSIVE"
        assert any("R3b-power" in r for r in verdict.reasons())

    def test_truthy_non_bool_strings_do_not_pass_r2_or_r3a(self, auditor):
        paper = self._valid_paper(base_rate_reported="false", raw_counts="false")
        verdict = auditor.audit(paper)
        assert verdict.verdict == "FAIL"
        assert any("R2-baserate" in r for r in verdict.reasons())
        assert any("R3a-counts" in r for r in verdict.reasons())
