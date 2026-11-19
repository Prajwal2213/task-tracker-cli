from sys import argv
import json
from datetime import datetime

def new_task(tasks, desc):
    task_id = max([task["id"] for task in tasks], default = 0) + 1

    now = datetime.now().isoformat()

    data = {
        "id": task_id,
        "desc" : desc,
        "status": "todo",
        "created_at": now,
        "updated_at": now
    }

    tasks.append(data)

    with open("data.json", "w") as file:
        json.dump(tasks, file, indent = 4)
        
    print("The Task id is {0}".format(task_id))
    
def update_task(id, desc, tasks):
    req_task = next((task for task in tasks if task["id"] == id), None)
    
    if req_task is None:
        print("task does not exits")
        return

    req_task["desc"] = desc
    req_task["updated_at"] = datetime.now().isoformat()
    try:
        with open("data.json", "w") as file:
            json.dump(tasks, file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("task not found")

def delete_task(id, tasks):
    req_task = next((task for task in tasks if task["id"] == id), None)
    
    if req_task is None:
        print("Task does not exist")
        return

    tasks = [task for task in tasks if task["id"] != id]
    
    with open("data.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print_list(tasks)

def mark_progress(task_id,tasks, status):

    req_task = next((task for task in tasks if task["id"] == task_id), None)

    if req_task is None:
        print("Task does not exist")
        return

    req_task["status"] = status[5:]

    with open("data.json", "w")as file:
        json.dump(tasks, file, indent = 4)

def print_list(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return

    print("\n" + "=" * 65)
    print(f"{'TASK ID':<12}{'DESCRIPTION':<35}{'STATUS':<15}")
    print("=" * 65)

    for task in tasks:
        print(f"{task['id']:<12}{task['desc'].capitalize():<35}{task['status'].upper():<15}")

    print("=" * 65)

def print_list_progress(tasks, status):
    if not tasks:
        print("\n No tasks found!")
        return

    progress_list = []

    for task in tasks:
        if task["status"] == status.lower():
            progress_list.append(task)

    print_list(progress_list)








def main():
    fun_call = argv[1].lower()

    if len(argv) > 2:
        if argv[2].isnumeric():
            task_id = int(argv[2])
            desc = argv[3] if len(argv) > 3 else None
        else:
            desc = argv[2]
            task_id = None
    
    try:
        with open("data.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
       
    if fun_call == "add":
        new_task(tasks, desc)
    elif fun_call == "update":
        update_task(task_id, desc, tasks)
        
    elif fun_call == "delete":
        delete_task(task_id, tasks)
    elif fun_call == "mark-in-progress" or fun_call == "mark-done":
        mark_progress(task_id, tasks, fun_call)
    if len(argv) == 2:
        print_list(tasks)
    elif len(argv) == 3:
        print_list_progress(tasks, argv[2])

    
if __name__ == "__main__":
    main()
    

    