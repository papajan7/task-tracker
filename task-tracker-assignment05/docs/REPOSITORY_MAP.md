# Repository Map and Baseline Context

## Entry points and modules

| Path | Responsibility |
|---|---|
| `app/cli.py` | CLI entry point and command dispatch |
| `app/models.py` | Task domain model and title validation |
| `app/service.py` | Add/list/update/delete use cases |
| `app/storage.py` | JSON load/save boundary |
| `app/strategies.py` | Created-time and status-priority ordering strategies |
| `tests/test_task_tracker.py` | Unit and regression tests |
| `AGENTS.md` | Coding-agent scope, safety boundaries and verification gates |

## Dependencies and scripts

- Runtime: Python 3.10+ standard library only; no third-party runtime dependencies.
- Test command: `python -m unittest discover -s tests -v`.
- Compile check: `python -m compileall -q app tests`.
- CLI help: `python -m app.cli --help`.
- There is no separate bundler/build system for this standard-library CLI project.

## Baseline snapshot

`baseline/app/` preserves the pre-mitigation implementation. It is intentionally retained for audit comparison, not used by the final CLI. The baseline had no automated test suite. Findings below are based on direct source inspection and reproduced behavior where noted.

## Baseline weaknesses observed

1. `baseline/app/service.py:add_task` accepts blank/whitespace titles without validation.
2. `baseline/app/service.py:update_status` accepts arbitrary status strings.
3. `baseline/app/service.py:update_status` silently saves and returns `None` when the task ID does not exist.
4. `baseline/app/storage.py:save` writes directly to the destination file; a process interruption during write can leave truncated JSON. This is a failure-mode risk inferred from the direct-write implementation, not a simulated crash test.
5. Baseline sorting behavior is embedded in conditional branches in `list_tasks`, so adding a new ordering mode expands the same method. This is a maintainability concern supported by the code structure.
6. Baseline has no repository-level agent operating instructions or automated tests.
