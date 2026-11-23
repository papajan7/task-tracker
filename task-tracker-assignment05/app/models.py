"""Domain models for the Task Tracker."""

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any


VALID_STATUSES = {"todo", "in_progress", "done"}


@dataclass(frozen=True)
class Task:
    id: int
    title: str
    status: str = "todo"
    created_at: str = ""

    @classmethod
    def create(cls, task_id: int, title: str) -> "Task":
        clean_title = title.strip() if isinstance(title, str) else ""
        if not clean_title:
            raise ValueError("Task title must not be empty.")
        return cls(
            id=task_id,
            title=clean_title,
            status="todo",
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        return cls(
            id=int(data["id"]),
            title=str(data["title"]),
            status=str(data.get("status", "todo")),
            created_at=str(data.get("created_at", "")),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
