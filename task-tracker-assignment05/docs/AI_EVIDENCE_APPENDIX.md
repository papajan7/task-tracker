# AI Evidence Appendix

## 1. AI assistant record

- **Assistant:** ChatGPT (GPT-6)
- **Date:** 23 November 2026
- **Purpose:** Interpret the official Assignment #05 brief, create a small testable repository, document the AI-assisted workflow, and verify the generated working copy.
- **Other AI tools:** DeepSeek was discussed as an option but was not used for the work recorded here.

## 2. Prompt and task log

The following is a concise record of the prompts/tasks actually given during this conversation (summarized without changing their intent):

| # | User prompt / task | Intended output |
|---|---|---|
| 1 | “по 5 ассайменту что надо делать?” with the Assignment #05 PDF attached | Extract the ten tasks, deliverables, submission format and deadline from the assignment brief. |
| 2 | “а его можно сделать в дипсике или сам сможешь сделать?” | Explain whether the assignment can be completed with ChatGPT and how AI assistance should be used. |
| 3 | “нету” (no existing project/repository) | Select a small project suitable for the assignment. |
| 4 | “давай ты лучше сделай мне и я загружу в гитхаб” | Create a Python CLI Task Tracker repository, including baseline, final implementation, tests and assignment documentation. |
| 5 | GitHub repository URL followed by “проверяй” | Review the uploaded repository against the assignment requirements. |
| 6 | “а у меня нету способов проверить так как нету вс кода давай перейдем к AI Evidence” | Prepare a transparent AI evidence appendix and verify what can be checked in the available working environment without requiring the user's local IDE. |

## 3. AI-generated outputs used

- Python CLI application modules in `app/`.
- Baseline snapshot in `baseline/`.
- Automated tests in `tests/`.
- Repository instructions in `AGENTS.md`.
- Requirements, repository map, pattern decision, risk register, agent-readiness audit, mitigation notes, background-agent safeguards, release decision and AI reflection in `docs/`.

## 4. Verification performed in the assistant's working environment

The assistant executed the following commands against the generated project working copy on 23 November 2026:

| Command | Actual result |
|---|---|
| `python -m unittest discover -s tests -v` | 8 tests passed; exit code 0 |
| `python -m compileall -q app tests` | Passed; exit code 0 |
| CLI smoke check using a temporary data file: add a task, then list tasks | Task creation and listing succeeded |

The corresponding command outputs are stored in `evidence/final_test_output.txt`, `evidence/compile_check.txt` and `evidence/cli_smoke_test.txt`. These are text logs from the assistant's working environment, not screenshots and not proof that the commands were run on the user's computer or on GitHub.

## 5. Human review and decisions

- The assistant generated the code and documentation; the repository owner should review the final GitHub contents before submission.
- The Strategy decision should be assessed against the actual size and needs of this small application; the pattern is included as a focused example, not claimed to be universally necessary.
- The two implemented mitigations are input/domain validation and safer JSON persistence using temporary-file replacement.
- No production deployment, external service, real credential or personal dataset was used.

## 6. Limitations and evidence boundaries

- The assistant can run commands in its own working environment, but this does not establish that the user's computer has Python configured or that the uploaded GitHub copy is byte-for-byte identical to the tested working copy.
- The text logs are not screenshots. If the instructor explicitly requires screenshots, they must be captured from an actual terminal session; do not present generated text logs as screenshots.
- No independent review by another person, CI run, cross-platform test, concurrency test or production security assessment is claimed.
- Update this appendix if the repository is changed after these checks. Do not claim any additional manual verification that was not performed.
