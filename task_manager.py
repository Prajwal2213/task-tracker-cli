
from datetime import datetime
from storage import save_task


def new_task(tasks, desc):
    task_id = max([task["id"] for task in tasks], default=0) + 1

    now = datetime.now().isoformat()

    data = {
        "id": task_id,
        "desc": desc,
        "status": "todo",
        "created_at": now,
        "updated_at": now
    }

    tasks.append(data)
    save_task(tasks)

    print("The Task id is {0}".format(task_id))


def update_task(task_id, desc, tasks):
    req_task = next(
        (task for task in tasks if task["id"] == task_id),
        None
    )

    if req_task is None:
        print("Task does not exist")
        return

    req_task["desc"] = desc
    req_task["updated_at"] = datetime.now().isoformat()

    save_task(tasks)
    print("Task updated successfully")


def delete_task(task_id, tasks):
    req_task = next(
        (task for task in tasks if task["id"] == task_id),
        None
    )

    if req_task is None:
        print("Task does not exist")
        return

    tasks[:] = [task for task in tasks if task["id"] != task_id]

    save_task(tasks)
    print("Task deleted successfully")


def mark_progress(task_id, tasks, status):
    req_task = next(
        (task for task in tasks if task["id"] == task_id),
        None
    )

    if req_task is None:
        print("Task does not exist")
        return

    if status == "mark-in-progress":
        req_task["status"] = "in-progress"

    elif status == "mark-done":
        req_task["status"] = "done"

    else:
        print("Invalid status")
        return

    req_task["updated_at"] = datetime.now().isoformat()

    save_task(tasks)
    print("Task status updated successfully")


def print_list(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return

    print("\n" + "=" * 65)
    print(f"{'TASK ID':<12}{'DESCRIPTION':<35}{'STATUS':<15}")
    print("=" * 65)

    for task in tasks:
        print(
            f"{task['id']:<12}"
            f"{task['desc'].capitalize():<35}"
            f"{task['status'].upper():<15}"
        )

    print("=" * 65)


def print_list_progress(tasks, status):
    progress_list = [
        task for task in tasks
        if task["status"] == status
    ]

    print_list(progress_list)
