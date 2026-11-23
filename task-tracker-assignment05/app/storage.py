"""JSON persistence for tasks."""

import json
import os
import tempfile
from pathlib import Path

from app.models import Task


class JsonTaskStorage:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Task data file contains invalid JSON: {self.path}") from exc
        if not isinstance(raw, list):
            raise ValueError("Task data must be a JSON array.")
        return [Task.from_dict(item) for item in raw]

    def save(self, tasks: list[Task]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps([task.to_dict() for task in tasks], indent=2, ensure_ascii=False)
        temp_name: str | None = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", encoding="utf-8", dir=self.path.parent,
                prefix=f".{self.path.name}.", suffix=".tmp", delete=False
            ) as temp_file:
                temp_name = temp_file.name
                temp_file.write(payload)
                temp_file.flush()
                os.fsync(temp_file.fileno())
            os.replace(temp_name, self.path)
        finally:
            if temp_name and os.path.exists(temp_name):
                os.unlink(temp_name)
