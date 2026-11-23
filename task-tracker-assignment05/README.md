# Task Tracker — Software Engineering Assignment #05

A small local command-line task tracker written in Python 3.10+ using only the standard library. It stores tasks in a JSON file and supports adding, listing, updating, and deleting tasks.

## Features

- Add tasks with non-empty titles (surrounding whitespace is trimmed).
- List tasks by status priority or creation time.
- Change status (`todo`, `in_progress`, `done`).
- Delete tasks by ID.
- Persist data in JSON using an atomic file-replacement strategy.

## Setup

1. Install Python 3.10 or newer.
2. Clone or download this repository.
3. No third-party runtime dependencies are required.

## Run

From the repository root:

```bash
python -m app.cli add "Prepare assignment"
python -m app.cli list
python -m app.cli status 1 done
python -m app.cli delete 1
```

Use a different data file with the global option placed before the command:

```bash
python -m app.cli --data-file ./data/tasks.json add "Review tests"
```

## Test

```bash
python -m unittest discover -s tests -v
```

## Repository contents

- `app/` — application source code.
- `tests/` — automated unit tests.
- `baseline/` — preserved simplified baseline implementation for comparison.
- `docs/` — assignment analysis and decision records.
- `evidence/` — captured command outputs from this working copy.
- `AGENTS.md` — operating instructions and safety boundaries for coding agents.

## Assignment note

The `baseline/` directory is the preserved pre-mitigation snapshot. The root `app/` directory is the reviewed final version. Test logs in `evidence/` are from commands actually run against the final version in this environment. Re-run the commands after cloning and replace or supplement evidence with your own screenshots if your instructor requires screenshots from your machine.
