---
name: math-modeling-contest-workflow
description: End-to-end workflow for mathematical modeling competitions, including CUMCM, MCM/ICM and similar problems. Use it to simplify a modeling problem, resolve answer-changing definitions, build and solve a sufficient model, perform one closed verification per subproblem, integrate results, or continue an existing contest workspace. Do not use it for ordinary single-formula homework or paper-only polishing when no modeling workflow is needed.
---

# Mathematical Modeling Contest Workflow

## Purpose

Finish contest modeling work efficiently and defensibly:

**题目简化 → 建模 → 求解 → 每小问一次封闭验证 → 必要修复回归 → DONE**

Preserve safeguards that can change the mathematical answer. Do not turn ordinary modeling into software-security review, meta-audit, or unlimited refinement. Paper writing remains outside the default scope.

## Authority and boundaries

1. Follow the user's current instruction, then project-local instructions, then this Skill.
2. The main agent alone controls scope, task assignment, repair, stage transitions, reopening, and completion.
3. Never invent source contents, runs, definitions, data, or validation conclusions.
4. Keep claims traceable to definitions, assumptions, formulas, code, runs, and checks.
5. Maintain concise project-level `状态账本.md` and `操作记录.md`. Preserve old audit files as history, but do not inherit their legacy gates when work is reopened under this protocol.

## Modes

- **Discussion:** answer only the requested analytical scope.
- **Complete execution:** simplify, model, solve, verify, repair if needed, integrate, and deliver.
- **Paper writing:** enter only when explicitly requested; then load `references/stages/70-paper-writing.md`.

Legacy `BLIND_REQUEST`, `BLIND_COMMIT`, or stage audits are historical evidence, not live gates.

## Action admission and impact

Before a nontrivial action, the main agent records internally: the exact task, the result or required deliverable it serves, A/B/C impact, finite output, and stopping point. Do not repeatedly narrate this record.

- **A — answer-changing:** can change a definition, feasible set, objective, constraint, result, optimum, or core conclusion. It blocks completion.
- **B — confidence-changing:** affects robustness, tolerance, sensitivity, or conclusion strength without currently changing the selected answer. Check within a stated bound, then disclose.
- **C — non-core:** engineering polish or meta-audit with no identified mathematical or required-deliverable impact. Record if useful; it never blocks, creates work, reopens a stage, or triggers verification.

User-requested work and reproducibility required for delivery are admissible even when they do not alter the answer.

## Progressive routing

| Situation | Read |
|---|---|
| New problem | `references/state-template.md`, `references/stages/00-whole-problem-intake.md` |
| Definitions | `references/stages/10-definition-audit.md` and relevant risk plugins |
| Model design | `references/stages/20-model-design.md` and relevant risk plugins |
| Solve | `references/stages/30-implementation-solve.md` |
| Partial information or cross-question reuse | `references/plugins/information-admissibility.md` |
| Closed verification | `references/stages/40-independent-audit.md` and both supervision references |
| Integration | `references/stages/50-cross-question-integration.md` |
| Delivery | `references/stages/60-result-delivery.md` |
| Skill maintenance | `references/rule-coverage.md`, `references/workflow-guide.md` |

## Reduced state machine

1. Stage 00 once: simplify the whole problem into inputs, outputs, dependencies, risks, and deliverables.
2. For each subproblem, run stages 10, 20, and 30 locally. These are work gates, not supervisor handshakes.
3. Stage 40 once: verify 1–3 closed propositions with tolerances and decision criteria.
4. If round 1 finds A, the main agent makes one targeted repair. Round 2 checks only the modification and direct dependencies.
5. After round 2, stop automatic iteration. A third round requires explicit `用户重新打开` authorization.
6. Run stages 50 and 60. Mark completed work `DONE` and stop unsolicited optimization.

Rounds are `0 / 1 / 2`; states are `进行中 / 验证中 / DONE / 用户重新打开`.

## Answer-changing safeguards

- Lock definitions, denominator, direction, units, boundary inclusion, precision, and rounding before coding.
- If plausible definitions agree on an example or symmetric case, construct a distinguishing counterexample.
- Translate every/exists/at least one/jointly/separately/cumulative/overlap into quantifiers or set operations.
- Do not decompose multi-object coverage without a valid decomposition argument.
- Compare the original decision space, model space, and program search space; prove restrictions lossless or label them restricted/heuristic.
- Preserve lexicographic or Pareto structure unless scalarization is justified.
- Back-substitute into original equations and hard constraints.
- Do not use a coarse grid alone to claim a continuous optimum or a picture alone to prove feasibility.
- Attach an honest evidence level to optimality, feasibility, coverage, stability, and significance claims.

Load only matching files from `references/plugins/`; plugins strengthen relevant checks but do not create audit stages.

## Answer validity gate

Before a subproblem can be marked `DONE`, require `ANSWER_VALIDITY_PASS = true` by checking three consistencies:

1. **MODEL == PROBLEM** - Definitions, objective, constraints, information assumptions, and quantifiers match the original problem. If ambiguity can change the answer, resolve it or state a conditional result.
2. **SOLVER == MODEL** - The implementation solves the stated model over its admissible space. Identify every discretization, sample grid, restricted candidate family, surrogate objective, and inherited assumption; prove it lossless or label the result restricted/approximate.
3. **EVIDENCE == CLAIM** - Validation tests the actual conclusion, not merely whether the code reproduces itself. Claims containing continuous, every, complete, global, minimum, maximum, unique, or optimal need evidence appropriate to those quantifiers.

Any failure that can change the answer is A and blocks `DONE`. Risk tags only identify which consistency is most vulnerable and what evidence is needed; they do not create new stages or long protocols.

For each core conclusion, use the strongest applicable evidence label:

- `PROVED / EXACT` - supported by a proof, exact derivation, exhaustive certificate, or equivalent guarantee;
- `NUMERICALLY VERIFIED` - independently checked within stated tolerances, without a stronger theorem;
- `HIGH-QUALITY FEASIBLE` - a strong feasible solution without a global-optimality guarantee;
- `HEURISTIC / APPROXIMATE` - dependent on an approximation, restricted family, sampling, or heuristic search.

Do not use `optimal`, `minimum`, `maximum`, `unique`, or `exact` more strongly than the recorded evidence permits.


## Information admissibility

Every executable decision, control, estimate, prediction, or optimization step may depend only on information legally available to that decision-maker at that time.

Set `INFO_RISK = ON` when a subproblem involves multiple actors, sensing or observation, communication or memory, online decisions, hidden states or parameters, simulation truth, explicit information limits, or cross-question solver reuse. Otherwise record `INFO_RISK = OFF` with a short reason such as `static full-information problem`.

When `INFO_RISK = ON`, read `references/plugins/information-admissibility.md`. Its information contract and three gates are answer-changing safeguards, not additional stages. Hidden truth may generate observations and evaluate outcomes, but it cannot enter a policy dependency chain unless the problem makes it observable.

## Closed verification

Use at most one verifier per subproblem. Give it only the original problem/data needed, 1–3 propositions, tolerances and criteria, plus allowed and forbidden scope.

It returns at most five A/B issues. Every issue states which result changes without a fix and how. It must not hide multiple genuine A issues merely because of the display limit; state that more A issues exist and narrow the follow-up check.

The verifier cannot modify official files, choose repairs, advance stages, declare completion, create agents, delegate, recursively audit, or inspect the verifier itself. The main agent alone acts on the report.

Use proof, hand calculation, a different derivation/algorithm, numerical recomputation, bounds, invariants, or exhaustive small cases in proportion to risk. Re-running the same evaluator is not independent evidence. If an independent thread is unavailable, use a different in-thread method, label the evidence lower, and continue unless A remains.

General software-security, integrity, or trusted-computing hardening is C by default unless explicitly requested or required for delivery.

## DONE

A subproblem is DONE when definitions/units are clear; the model matches objective, decision space, and hard constraints; a solution exists; back-substitution passes; one proportionate independent check supports the core result; no unresolved A remains; and B limitations are disclosed. If `INFO_RISK = ON`, `INFORMATION_PASS` must also be true.

`ANSWER_VALIDITY_PASS` also requires the core conclusion's evidence label to be recorded.

After DONE, do not start new optimization, audit, or a third verification round without explicit user reopening. Deliver the result, evidence level, limitations, and reproducible entry points.
