"""Automated tests for Task Tracker behavior and mitigations."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.models import Task
from app.service import TaskService
from app.storage import JsonTaskStorage
from app.strategies import CreatedAtStrategy, PriorityStatusStrategy


class TaskServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name) / "data" / "tasks.json"
        self.service = TaskService(JsonTaskStorage(self.path))

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_add_task_trims_title_and_persists(self) -> None:
        task = self.service.add_task("  Prepare report  ")
        self.assertEqual(task.title, "Prepare report")
        self.assertEqual(self.service.list_tasks()[0].title, "Prepare report")

    def test_rejects_empty_or_whitespace_title(self) -> None:
        for title in ("", "   ", "\n\t"):
            with self.subTest(title=repr(title)):
                with self.assertRaises(ValueError):
                    self.service.add_task(title)
        self.assertEqual(self.service.list_tasks(), [])

    def test_rejects_invalid_status_without_changing_file(self) -> None:
        task = self.service.add_task("Review code")
        before = self.path.read_text(encoding="utf-8")
        with self.assertRaises(ValueError):
            self.service.update_status(task.id, "finished-ish")
        self.assertEqual(self.path.read_text(encoding="utf-8"), before)

    def test_updates_status_and_deletes_task(self) -> None:
        task = self.service.add_task("Run tests")
        updated = self.service.update_status(task.id, "done")
        self.assertEqual(updated.status, "done")
        self.service.delete_task(task.id)
        self.assertEqual(self.service.list_tasks(), [])

    def test_missing_task_raises_key_error(self) -> None:
        with self.assertRaises(KeyError):
            self.service.update_status(404, "done")
        with self.assertRaises(KeyError):
            self.service.delete_task(404)

    def test_priority_strategy_orders_active_tasks_first(self) -> None:
        tasks = [
            Task(1, "Done", "done", "2026-01-01"),
            Task(2, "Todo", "todo", "2026-01-02"),
            Task(3, "In progress", "in_progress", "2026-01-03"),
        ]
        self.assertEqual(
            [task.id for task in PriorityStatusStrategy().sort(tasks)], [3, 2, 1]
        )
        self.assertEqual(
            [task.id for task in CreatedAtStrategy().sort(tasks)], [1, 2, 3]
        )

    def test_invalid_json_is_reported_clearly(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text("{not-json", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "invalid JSON"):
            self.service.list_tasks()

    def test_save_uses_atomic_replace(self) -> None:
        storage = JsonTaskStorage(self.path)
        task = Task.create(1, "Atomic save")
        with patch("app.storage.os.replace", wraps=__import__("os").replace) as replace:
            storage.save([task])
            replace.assert_called_once()
        self.assertEqual(json.loads(self.path.read_text(encoding="utf-8"))[0]["title"], "Atomic save")


if __name__ == "__main__":
    unittest.main()
