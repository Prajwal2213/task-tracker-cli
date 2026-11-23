
import json
import main


# Sample task data for testing
def sample_tasks():
    return [
        {
            "id": 1,
            "desc": "Learn Python",
            "status": "todo",
            "created_at": "2026-11-19T08:00:00",
            "updated_at": "2026-11-19T08:00:00"
        },
        {
            "id": 2,
            "desc": "Build REST API",
            "status": "in-progress",
            "created_at": "2026-11-19T08:00:00",
            "updated_at": "2026-11-19T08:00:00"
        },
        {
            "id": 3,
            "desc": "Complete project",
            "status": "done",
            "created_at": "2026-11-19T08:00:00",
            "updated_at": "2026-11-19T08:00:00"
        }
    ]


# 1. Test adding a new task
def test_new_task(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    tasks = []

    main.new_task(tasks, "Learn Python")

    with open("data.json", "r") as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["id"] == 1
    assert data[0]["desc"] == "Learn Python"
    assert data[0]["status"] == "todo"
    assert "created_at" in data[0]
    assert "updated_at" in data[0]


# 2. Test updating an existing task
def test_update_task(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    tasks = sample_tasks()

    main.update_task(1, "Learn FastAPI", tasks)

    with open("data.json", "r") as file:
        data = json.load(file)

    assert data[0]["desc"] == "Learn FastAPI"
    assert len(data) == 3


# 3. Test updating a task that does not exist
def test_update_invalid_task(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    tasks = sample_tasks()

    main.update_task(10, "New Description", tasks)

    captured = capsys.readouterr()

    assert "Task does not exist" in captured.out


# 4. Test deleting an existing task
def test_delete_task(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    tasks = sample_tasks()

    main.delete_task(2, tasks)

    with open("data.json", "r") as file:
        data = json.load(file)

    assert len(data) == 2
    assert all(task["id"] != 2 for task in data)


# 5. Test deleting a task that does not exist
def test_delete_invalid_task(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    tasks = sample_tasks()

    main.delete_task(10, tasks)

    captured = capsys.readouterr()

    assert "Task does not exist" in captured.out


# 6. Test marking a task as in-progress
def test_mark_in_progress(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    tasks = sample_tasks()

    main.mark_progress(1, tasks, "in-progress")

    with open("data.json", "r") as file:
        data = json.load(file)

    assert data[0]["status"] == "in-progress"


# 7. Test marking a task as done
def test_mark_done(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    tasks = sample_tasks()

    main.mark_progress(1, tasks, "done")

    with open("data.json", "r") as file:
        data = json.load(file)

    assert data[0]["status"] == "done"


# 8. Test marking an invalid task
def test_mark_invalid_task(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    tasks = sample_tasks()

    main.mark_progress(10, tasks, "done")

    captured = capsys.readouterr()

    assert "Task does not exist" in captured.out


# 9. Test displaying all tasks
def test_print_list(capsys):
    tasks = sample_tasks()

    main.print_list(tasks)

    captured = capsys.readouterr()

    assert "Learn Python" in captured.out
    assert "Build REST API" in captured.out
    assert "Complete project" in captured.out


# 10. Test displaying an empty task list
def test_print_empty_list(capsys):
    tasks = []

    main.print_list(tasks)

    captured = capsys.readouterr()

    assert "No tasks found!" in captured.out


# 11. Test filtering tasks by status
def test_print_list_progress(capsys):
    tasks = sample_tasks()

    main.print_list_progress(tasks, "done")

    captured = capsys.readouterr()

    assert "Complete project" in captured.out
    assert "Learn Python" not in captured.out
    assert "Build REST API" not in captured.out


# 12. Test filtering tasks by in-progress status
def test_print_in_progress(capsys):
    tasks = sample_tasks()

    main.print_list_progress(tasks, "in-progress")

    captured = capsys.readouterr()

    assert "Build REST API" in captured.out
    assert "Learn Python" not in captured.out
    assert "Complete project" not in captured.out


# 13. Test invalid status filtering
def test_invalid_status(capsys):
    tasks = sample_tasks()

    main.print_list_progress(tasks, "pending")

    captured = capsys.readouterr()

    assert "Invalid status" in captured.out
