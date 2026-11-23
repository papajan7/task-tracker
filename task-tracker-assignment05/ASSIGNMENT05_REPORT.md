# Software Engineering — Assignment #05

**Project:** Task Tracker (Python CLI)  
**Reviewed version:** Final working copy  
**AI assistant:** ChatGPT (GPT-6)  
**Date:** 23 November 2026

## Executive summary

This assignment audits and improves a small local task-tracking application. The repository preserves a baseline implementation in `baseline/app/` and provides the reviewed implementation in `app/`. The final version adds domain validation, explicit error handling, atomic JSON persistence, a focused Strategy refactoring for task ordering, automated tests, and repository-specific AI-agent instructions.

## Work completed

1. **Baseline and context:** documented modules, entry points, dependencies, commands, baseline weaknesses, and the absence of baseline automated tests.
2. **Agent instructions:** created root `AGENTS.md` with setup, architecture, safe commands, coding conventions, prohibited actions, and human review gates.
3. **Pattern decision:** applied one focused Strategy refactoring to isolate task ordering behavior; see `docs/PATTERN_DECISION.md`.
4. **Read-only risk review:** evaluated six findings across correctness, reliability, maintainability, agent operations, and verification; see `docs/RISK_REGISTER.md`.
5. **Risk register:** scored likelihood and impact from 1–3 and documented mitigations, owners, verification, and residual risk.
6. **Agent readiness:** assigned Level 2 — Documented; Level 3 is not claimed because instructions are not technically enforced and CI/platform evidence is missing.
7. **Mitigation and verification:** implemented domain/input validation and atomic persistence; added regression tests and reran checks.
8. **Background-agent safeguards:** specified a hypothetical isolated task, file scope, commands, time limit, prohibited operations, required artifacts, and human approval.
9. **Release decision:** CONDITIONAL for local educational use only.
10. **AI reflection:** included a 283-word reflection in `docs/AI_REFLECTION.md`.

## Verification results

- `python -m unittest discover -s tests -v` — **8 tests passed**.
- `python -m compileall -q app tests` — **PASS**.
- CLI smoke test — add, list, update status and list again all completed successfully.
- Baseline automated test suite — none existed; this is documented as a gap, not a pass.

See `evidence/` for command output. These are command logs, not screenshots.

## Acceptance criteria

See `docs/ACCEPTANCE_CRITERIA.md`. The final test suite covers title validation, status validation, missing task handling, CRUD behavior, sorting, invalid JSON handling, and atomic replacement invocation.

## Release conclusion

**CONDITIONAL**: suitable as a local educational CLI with synthetic data. Not approved for production or concurrent multi-user use. Outstanding limitations include no file locking, no CI, no cross-platform test matrix, and limited schema validation for manually edited JSON.

## Submission note

Before submitting, review the content, upload the repository to your own GitHub account, and ensure the repository link is accessible to the instructor. Add screenshots from your own terminal if required by the instructor. Do not describe unperformed checks as completed.
