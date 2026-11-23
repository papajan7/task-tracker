"""Sorting strategies used by the task listing service."""

from typing import Protocol

from app.models import Task


class TaskSortStrategy(Protocol):
    def sort(self, tasks: list[Task]) -> list[Task]:
        """Return tasks in the strategy's order without mutating the input."""


class CreatedAtStrategy:
    def sort(self, tasks: list[Task]) -> list[Task]:
        return sorted(tasks, key=lambda task: (task.created_at, task.id))


class PriorityStatusStrategy:
    """Show unfinished work first, then in-progress work, then completed work."""

    _rank = {"in_progress": 0, "todo": 1, "done": 2}

    def sort(self, tasks: list[Task]) -> list[Task]:
        return sorted(tasks, key=lambda task: (self._rank.get(task.status, 99), task.id))
