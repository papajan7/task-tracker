"""Application use cases for creating and managing tasks."""

from app.models import VALID_STATUSES, Task
from app.storage import JsonTaskStorage
from app.strategies import CreatedAtStrategy, TaskSortStrategy


class TaskService:
    def __init__(self, storage: JsonTaskStorage) -> None:
        self.storage = storage

    def list_tasks(self, strategy: TaskSortStrategy | None = None) -> list[Task]:
        tasks = self.storage.load()
        return (strategy or CreatedAtStrategy()).sort(tasks)

    def add_task(self, title: str) -> Task:
        tasks = self.storage.load()
        next_id = max((task.id for task in tasks), default=0) + 1
        task = Task.create(next_id, title)
        self.storage.save([*tasks, task])
        return task

    def update_status(self, task_id: int, status: str) -> Task:
        if status not in VALID_STATUSES:
            allowed = ", ".join(sorted(VALID_STATUSES))
            raise ValueError(f"Invalid status '{status}'. Choose one of: {allowed}.")
        tasks = self.storage.load()
        updated: list[Task] = []
        result: Task | None = None
        for task in tasks:
            if task.id == task_id:
                result = Task(task.id, task.title, status, task.created_at)
                updated.append(result)
            else:
                updated.append(task)
        if result is None:
            raise KeyError(f"Task with id {task_id} was not found.")
        self.storage.save(updated)
        return result

    def delete_task(self, task_id: int) -> None:
        tasks = self.storage.load()
        remaining = [task for task in tasks if task.id != task_id]
        if len(remaining) == len(tasks):
            raise KeyError(f"Task with id {task_id} was not found.")
        self.storage.save(remaining)
