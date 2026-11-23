# Agent Instructions

## Purpose
This repository is a small educational CLI task tracker. It is not a production service and must only use synthetic local task data.

## Architecture
- `app/models.py`: immutable Task domain model and input/status constraints.
- `app/storage.py`: JSON persistence boundary; writes use a temporary file and `os.replace`.
- `app/service.py`: task use cases and validation orchestration.
- `app/strategies.py`: interchangeable task ordering strategies.
- `app/cli.py`: argument parsing and terminal presentation.
- `tests/`: standard-library `unittest` tests.

## Setup and safe commands
- Python 3.10+; no third-party runtime packages.
- Run tests: `python -m unittest discover -s tests -v`.
- Run CLI: `python -m app.cli --help`.
- Build/package check: `python -m compileall -q app tests`.
- Use temporary directories for tests. Do not use real user data.

## Coding conventions
- Follow PEP 8 and use type hints for public methods.
- Keep domain rules in `models.py` / `service.py`, persistence in `storage.py`, and terminal I/O in `cli.py`.
- Prefer small functions and immutable domain objects.
- Add or update tests for behavior changes.
- Do not add a design pattern without a concrete maintainability justification.

## Permissions and review gates
Allowed: inspect files, run tests/compile checks, edit source and documentation in a dedicated working branch, and add tests.
Forbidden without explicit human approval: access or add secrets, change production systems, deploy, publish releases, run destructive shell commands, delete user data, modify files outside this repository, or add/change dependencies.

## Required agent workflow
1. Read this file and `README.md` before editing.
2. Inspect the relevant code and existing tests.
3. State the intended files and rationale before making broad changes.
4. Make the smallest focused change.
5. Run the relevant tests and full test suite.
6. Report exact commands, results, changed files, limitations, and any tests not run.
7. Never claim a test passed unless its command was actually executed successfully.
8. Human review is required before merge, release, or deployment.
