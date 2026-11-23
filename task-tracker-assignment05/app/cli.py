"""Command-line interface for Task Tracker."""

import argparse
import sys

from app.service import TaskService
from app.storage import JsonTaskStorage
from app.strategies import PriorityStatusStrategy


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A small local task tracker.")
    parser.add_argument("--data-file", default="tasks.json", help="Path to the local JSON data file")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="Add a task")
    add.add_argument("title", help="Task title")

    commands.add_parser("list", help="List tasks")

    status = commands.add_parser("status", help="Change a task status")
    status.add_argument("task_id", type=int)
    status.add_argument("value", choices=["todo", "in_progress", "done"])

    delete = commands.add_parser("delete", help="Delete a task")
    delete.add_argument("task_id", type=int)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    service = TaskService(JsonTaskStorage(args.data_file))
    try:
        if args.command == "add":
            task = service.add_task(args.title)
            print(f"Added #{task.id}: {task.title}")
        elif args.command == "list":
            tasks = service.list_tasks(PriorityStatusStrategy())
            if not tasks:
                print("No tasks yet.")
            for task in tasks:
                print(f"#{task.id} [{task.status}] {task.title}")
        elif args.command == "status":
            task = service.update_status(args.task_id, args.value)
            print(f"Updated #{task.id} to {task.status}")
        elif args.command == "delete":
            service.delete_task(args.task_id)
            print(f"Deleted #{args.task_id}")
        return 0
    except (ValueError, KeyError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
