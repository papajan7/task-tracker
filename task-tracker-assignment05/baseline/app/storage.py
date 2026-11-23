"""Baseline persistence: writes directly to the target file."""

import json
from pathlib import Path

from app.models import Task


class JsonTaskStorage:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []
        return [Task(**item) for item in json.loads(self.path.read_text(encoding="utf-8"))]

    def save(self, tasks: list[Task]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps([task.__dict__ for task in tasks], indent=2), encoding="utf-8"
        )
