# Plugin: Information admissibility

Trigger when `INFO_RISK = ON`; do not create this audit for a static full-information problem.

## Invariant and contract

An executable decision must have the form `action = policy(admissible_information)`. Keep the dependency order `truth -> observation -> information -> decision`; a direct or indirect `truth -> decision` edge is illegal unless the truth is explicitly observable.

Record only:

- World truth.
- What each decision-maker can observe.
- Information that may be shared or remembered.
- Information forbidden to the policy.

## Three gates

1. **Before modeling — INFORMATION_GATE:** every policy input has an explicit legal source. Missing or unavailable information that can change the answer is A and blocks `MODEL_PASS`.
2. **After solving — POLICY_DEPENDENCY_GATE:** inspect the dependency chain of each executable decision. Simulation or hidden truth may generate observations and evaluate results, but must not influence the policy directly or indirectly. A violation makes `SOLVE_PASS = false`.
3. **At completion — INFORMATION_PASS:** confirm that all policy inputs have legal sources; hidden truth does not enter policy dependencies; communication, memory, timing, and actor-role restrictions are respected; and reused components still satisfy their information assumptions.

## Information-equivalence test

When applicable, construct or reason about two worlds with identical admissible information but different hidden truth. A deterministic policy must make the same decision; a randomized policy must have the same conditional distribution. Failure is A and makes `INFORMATION_PASS = false`.

Cross-question reuse never inherits assumptions automatically. Revalidate required observations, parameters, roles, timing, communication, and memory; if they no longer hold, reuse only the valid mathematical relation, not the solver or policy.
