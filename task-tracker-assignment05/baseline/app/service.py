"""Baseline service before assignment mitigations and refactoring."""

from app.models import Task
from app.storage import JsonTaskStorage


class TaskService:
    def __init__(self, storage: JsonTaskStorage) -> None:
        self.storage = storage

    def add_task(self, title: str) -> Task:
        tasks = self.storage.load()
        task = Task(max((item.id for item in tasks), default=0) + 1, title)
        self.storage.save([*tasks, task])
        return task

    def update_status(self, task_id: int, status: str) -> Task:
        tasks = self.storage.load()
        result = None
        updated = []
        for task in tasks:
            if task.id == task_id:
                task.status = status
                result = task
            updated.append(task)
        self.storage.save(updated)
        return result

    def list_tasks(self, sort_by: str = "id") -> list[Task]:
        tasks = self.storage.load()
        if sort_by == "title":
            tasks.sort(key=lambda task: task.title.lower())
        elif sort_by == "status":
            tasks.sort(key=lambda task: task.status)
        else:
            tasks.sort(key=lambda task: task.id)
        return tasks
