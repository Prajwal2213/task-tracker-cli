
import argparse

from storage import load_tasks
from task_manager import (
    new_task,
    update_task,
    delete_task,
    mark_progress,
    print_list,
    print_list_progress
)


def main():
    parser = argparse.ArgumentParser(
        description="Task Tracker CLI"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("desc", nargs="+")

    # Update command
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("desc", nargs="+")

    # Delete command
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    # Mark in-progress
    progress_parser = subparsers.add_parser("mark-in-progress")
    progress_parser.add_argument("id", type=int)

    # Mark done
    done_parser = subparsers.add_parser("mark-done")
    done_parser.add_argument("id", type=int)

    # List command
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument(
        "status",
        nargs="?",
        choices=["todo", "in-progress", "done"]
    )

    args = parser.parse_args()

    tasks = load_tasks()

    if args.command == "add":
        desc = " ".join(args.desc)
        new_task(tasks, desc)

    elif args.command == "update":
        desc = " ".join(args.desc)
        update_task(args.id, desc, tasks)

    elif args.command == "delete":
        delete_task(args.id, tasks)

    elif args.command == "mark-in-progress":
        mark_progress(args.id, tasks, args.command)

    elif args.command == "mark-done":
        mark_progress(args.id, tasks, args.command)

    elif args.command == "list":
        if args.status:
            print_list_progress(tasks, args.status)
        else:
            print_list(tasks)


if __name__ == "__main__":
    main()
