import json
from json import JSONDecodeError


def load_task():
    try:
        with open('data.json', 'r') as f:
            tasks = json.load(f)
            return tasks
    except(FileNotFoundError, JSONDecodeError):
        return {}



def save_task(tasks):
    with open('data.json', 'w') as f:
        json.dump(tasks, f, indent = 4)