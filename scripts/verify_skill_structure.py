from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "SKILL.md",
    "references/state-template.md",
    "references/workflow-guide.md",
    "references/rule-coverage.md",
    "references/plugins/information-admissibility.md",
    "references/supervision/independent-supervisor.md",
    "references/supervision/audit-packet-template.md",
    "evals/evals.json",
    *[f"references/stages/{name}" for name in (
        "00-whole-problem-intake.md",
        "10-definition-audit.md",
        "20-model-design.md",
        "30-implementation-solve.md",
        "40-independent-audit.md",
        "50-cross-question-integration.md",
        "60-result-delivery.md",
        "70-paper-writing.md",
    )],
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        require((ROOT / rel).is_file(), f"missing: {rel}", errors)

    if errors:
        print("\n".join(errors))
        return 1

    skill = read("SKILL.md")
    supervisor = read("references/supervision/independent-supervisor.md")
    template = read("references/supervision/audit-packet-template.md")
    state = read("references/state-template.md")
    stage40 = read("references/stages/40-independent-audit.md")
    information = read("references/plugins/information-admissibility.md")

    require("name: math-modeling-contest-workflow" in skill, "frontmatter name changed", errors)
    require("题目简化" in skill and "DONE" in skill, "reduced workflow missing", errors)
    require("VERIFY_REQUEST" in template and "VERIFY_REPORT" in template, "protocol 2.0 interface missing", errors)
    require("1–3" in supervisor and "最多五项" in supervisor, "closed verifier limits missing", errors)
    require("不得创建或委派" in supervisor, "recursive delegation prohibition missing", errors)
    require(all(token in state for token in ("进行中", "验证中", "DONE", "用户重新打开")), "state set incomplete", errors)
    require(all(token in state for token in ("A/B/C", "具体影响说明", "证据", "处理决定")), "issue schema incomplete", errors)
    require("轮次 2" in stage40 and "第三轮" in stage40, "two-round stop rule missing", errors)
    require(all(token in skill for token in ("INFO_RISK", "INFORMATION_PASS")), "information routing missing", errors)
    require(all(token in information for token in ("INFORMATION_GATE", "POLICY_DEPENDENCY_GATE", "Information-equivalence")), "information gates missing", errors)
    require(all(token in skill for token in ("ANSWER_VALIDITY_PASS", "MODEL == PROBLEM", "SOLVER == MODEL", "EVIDENCE == CLAIM")), "answer validity gate missing", errors)
    require(all(token in state for token in ("PROVED / EXACT", "NUMERICALLY VERIFIED", "HIGH-QUALITY FEASIBLE", "HEURISTIC / APPROXIMATE")), "claim labels missing", errors)

    data = json.loads(read("evals/evals.json"))
    ids = {case["id"] for case in data.get("cases", [])}
    expected_ids = {
        "definition-ambiguity-is-a",
        "multi-object-quantifier-is-a",
        "hidden-truth-policy-dependency-is-a",
        "information-equivalence-detects-leak",
        "cross-question-reuse-revalidates-information",
        "full-information-skips-information-audit",
        "tolerance-is-bounded-b",
        "security-meta-work-is-c",
        "verifier-cannot-delegate",
        "done-stops-third-round",
        "objective-mismatch-is-a",
        "sampled-safe-is-not-continuously-safe",
        "restricted-heuristic-is-not-global-optimum",
    }
    require(ids == expected_ids, f"targeted eval ids differ: {sorted(ids)}", errors)

    if errors:
        print("STRUCTURE CHECK FAILED")
        print("\n".join(f"- {item}" for item in errors))
        return 1

    print("STRUCTURE CHECK PASSED")
    print(f"protocol=2.0-reduced; targeted_scenarios={len(ids)}; stages=00-70")
    return 0


if __name__ == "__main__":
    sys.exit(main())
