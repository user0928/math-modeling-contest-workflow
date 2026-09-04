# Math Modeling Contest Workflow

An end-to-end Codex skill for mathematical modeling competitions such as CUMCM and MCM/ICM. It helps turn a contest problem into a defensible sequence of definition checks, model design, implementation, bounded independent verification, integration, and delivery.

## What it provides

- A reduced stage workflow from whole-problem intake through result delivery
- Answer-validity gates covering problem/model, model/solver, and evidence/claim consistency
- Risk-focused reference modules for information admissibility, geometry, multi-objective models, piecewise rules, spatial non-overlap, and related cases
- A bounded independent-verification protocol that avoids endless audit loops
- Targeted evaluation cases and a dependency-free structure check

## Install

Clone this repository into your Codex skills directory:

```powershell
git clone https://github.com/user0928/math-modeling-contest-workflow.git "$env:USERPROFILE\.codex\skills\math-modeling-contest-workflow"
```

Restart Codex after installation so the skill is discovered.

## Use

Invoke the skill explicitly when you want the complete workflow:

```text
Use $math-modeling-contest-workflow to solve this contest problem and keep a reproducible state ledger.
```

Codex may also select it automatically for end-to-end modeling-contest work. Ordinary single-formula homework and paper-only polishing are intentionally outside its default scope.

## Repository structure

```text
SKILL.md                 Main routing and operating rules
references/stages/       Stage-specific workflow guidance
references/plugins/      Risk-specific checks loaded only when relevant
references/supervision/  Independent verification protocol
evals/                   Targeted behavior cases and benchmark summary
scripts/                 Dependency-free structural validation
```

## Validate

```powershell
python scripts/verify_skill_structure.py
```

The repository also runs this validation automatically on pushes and pull requests.

## Maintenance

Keep `SKILL.md` concise and route conditional detail into focused references. When changing behavior, update the corresponding evaluation case and run the validation script before committing.
