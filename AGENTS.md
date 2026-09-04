# Repository instructions

- Use UTF-8 for all text files.
- Preserve the reduced workflow and its answer-changing safeguards.
- Keep conditional detail in focused files under `references/`; avoid duplicating it in `SKILL.md`.
- When behavior changes, update the matching cases in `evals/evals.json`.
- Before committing, run `python scripts/verify_skill_structure.py` and the Codex `quick_validate.py` checker when available.
- Do not use recursive or batch deletion commands. Delete only one explicit file path at a time.
