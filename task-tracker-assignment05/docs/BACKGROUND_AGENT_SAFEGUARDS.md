# Background Agent Safeguards (Hypothetical Task)

## Example asynchronous task

Ask a background coding agent to add a `due_date` field to tasks, with unit tests and documentation. This is a design exercise; no paid background-agent service was launched.

## Isolation and scope

- Create a dedicated branch or disposable Git worktree named `agent/due-date-field` from the reviewed baseline commit.
- Allowed files: `app/models.py`, `app/service.py`, `tests/`, and relevant `docs/` files. Any other file requires human approval.
- Allowed commands: inspect/list files, `python -m unittest discover -s tests -v`, `python -m compileall -q app tests`, and `git diff` / `git status`.
- Time limit: one bounded work session (maximum 30 minutes), then stop and report.
- No network access, secret access, production access, deployment, release, or dependency installation.
- Prohibited: destructive shell commands, deleting user data, force-pushing, modifying Git history, changing CI/repository settings, or committing directly to the default branch.

## Required outputs

1. Short change summary and list of changed files.
2. Complete Git diff.
3. Test log with exact commands and pass/fail totals.
4. Compile check result.
5. Risk notes, assumptions, and any untested cases.

## Human review and failure handling

A maintainer reviews the diff and reruns tests before merge. The agent cannot merge or deploy. If tests fail, the agent reports the failure and stops rather than weakening tests. If scope is exceeded or unexpected files change, discard the worktree/branch and restart from the clean baseline. Rollback is performed by not merging the branch or reverting the reviewed commit; never by destructive cleanup of user data.
