"""Logic Module: Handles core data processing for task management."""

# -- Task Operations --

"""Creates a new task, appends it to the list, and returns the updated ID."""
def add_task(tasks, last_id, title, description):
    new_id = last_id + 1
    new_task = {"id": new_id, "title": title, "description": description, "pending": True}
    tasks.append(new_task)
    return new_id

"""Updates the task status to complete using its visual index."""
def mark_task_as_complete(tasks, option):
    tasks[int(option) - 1]["pending"] = False

"""Deletes a task from the list based on its index."""
def remove_task(tasks, option):
    del tasks[int(option) - 1]

# -- Selection Validation --

"""Generates a list of valid options filtered by pending tasks."""
def options_validation_complete_task(tasks):
    options = ["b", "e"]
    for i in range(len(tasks)):
        if tasks[i]["pending"]:
            options.append(str(i+1))
    return options

"""Generates a list of valid options based on the tasks' visual indices"""
def options_validation_delete_task(tasks):
    options = ["b", "e"]
    for i in range(len(tasks)):
        options.append(str(i+1))
    return options