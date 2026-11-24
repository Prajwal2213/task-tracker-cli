
# Task Tracker CLI

A simple command-line task tracker built with Python. Manage your tasks with statuses like **todo**, **in-progress**, and **done**, all persisted in a local JSON file.

## Features

- **Add tasks** — Create new tasks with a description.
- **Update tasks** — Modify the description of an existing task.
- **Delete tasks** — Remove tasks by their ID.
- **Track progress** — Mark tasks as `in-progress` or `done`.
- **List tasks** — View all tasks or filter by status (`todo`, `in-progress`, `done`).
- **Persistent storage** — Tasks are saved to `data.json` and survive between sessions.

## Requirements

- Python 3.6+
- No external dependencies — uses only the Python standard library.

## Installation

Clone or download the project, then navigate to the project directory:

```bash
cd task_tracker_cli
```

That's it — no `pip install` needed.

## Usage

Run the CLI with `python main.py` followed by a subcommand:

### Add a task

```bash
python main.py add "Learn Python"
```

### Update a task

```bash
python main.py update 1 "Learn FastAPI"
```

### Delete a task

```bash
python main.py delete 1
```

### Mark a task as in-progress

```bash
python main.py mark-in-progress 1
```

### Mark a task as done

```bash
python main.py mark-done 1
```

### List all tasks

```bash
python main.py list
```

### List tasks by status

```bash
python main.py list todo
python main.py list in-progress
python main.py list done
```

## Project Structure

```
task_tracker_cli/
├── main.py            # CLI entry point (argparse)
├── task_manager.py    # Core task operations (CRUD, status updates)
├── storage.py         # JSON file read/write utilities
├── data.json          # Task data storage (auto-generated)
├── tests/
│   └── test_main.py   # Pytest test suite
└── README.md          # This file
```

## Running Tests

The project uses `pytest`. Install it and run:

```bash
pip install pytest
pytest
```

## Data Format

Tasks are stored in `data.json` as a JSON array. Each task has the following fields:

```json
{
    "id": 1,
    "desc": "Learn Python",
    "status": "todo",
    "created_at": "2026-11-19T08:00:00",
    "updated_at": "2026-11-19T08:00:00"
}
```

- **id** — Auto-incremented unique identifier.
- **desc** — Task description.
- **status** — One of `todo`, `in-progress`, or `done`.
- **created_at** / **updated_at** — ISO 8601 timestamps.
