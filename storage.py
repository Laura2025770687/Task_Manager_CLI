"""Storage Module: Handles data persistence and file operations using JSON format."""

import json
import os

"""Loads the file and retrieves the stored task data."""
def open_tasks_archive():
    try:
        if not os.path.exists("Tasks.json"):
            return {"tasks": [], "last_id": 0}
        with open("Tasks.json", encoding="utf-8") as dt:
            return json.load(dt)
    except json.JSONDecodeError:
        return {"tasks": [], "last_id": 0}

"""Writes and saves the updated task list and last ID to the JSON file."""
def save_tasks_archive(tasks, last_id):
    data = {"tasks": tasks, "last_id": last_id}
    with open("Tasks.json", "w", encoding="utf-8") as dt:
        json.dump(data, dt, indent=4, ensure_ascii=False)
