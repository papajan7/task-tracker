# Acceptance Criteria

The following criteria were defined before final changes and must remain true:

1. A user can add a task with a non-empty title; leading/trailing whitespace is removed.
2. A task status can only be `todo`, `in_progress`, or `done`.
3. A user can list and delete tasks; requesting a missing task produces a clear error rather than silently succeeding.
4. Task data survives process restarts through the JSON storage file.
5. A failed or interrupted persistence write should not expose a partially written target JSON file; persistence replaces the target only after a complete temporary write.
