# AI Evidence Appendix

## Tool record

- Assistant: ChatGPT (GPT-6)
- Date: 23 November 2026
- Purpose: interpret the supplied Assignment #05 brief; plan a small testable repository; draft implementation and audit documentation.

## Prompt summary

1. Summarize the required tasks and deliverables from the supplied Assignment #05 PDF.
2. Propose a small project suitable for the assignment.
3. Implement a Python CLI task tracker with tests, baseline snapshot, repository instructions, risk register, readiness audit, mitigation records, safeguards, release decision, and AI reflection.

## Outputs used

- Python source modules under `app/`.
- Unit tests under `tests/`.
- Baseline snapshot under `baseline/app/`.
- Assignment analysis under `docs/` and operating boundaries in `AGENTS.md`.

## Human verification performed in this working copy

- Inspected the source and test files after creation.
- Ran `python -m unittest discover -s tests -v` and recorded the actual result in `evidence/final_test_output.txt`.
- Ran `python -m compileall -q app tests` and recorded the command result in `evidence/compile_check.txt`.
- Ran CLI smoke checks and recorded output in `evidence/cli_smoke_test.txt`.

## Limitations

This appendix records the AI-assisted workflow in this conversation. It is not a screenshot of a third-party AI application. The repository author should update this record if additional tools, prompts, or manual changes are used before submission.
