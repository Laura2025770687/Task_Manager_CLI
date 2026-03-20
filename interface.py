"""
Interface Module: Manages the visual presentation and user input collection.
Implements terminal-based UI patterns and cross-platform screen management.
"""

import os
import time
import platform

"""
Clears the terminal window based on the current Operating System.
Detects 'Windows' or Unix-like systems (Linux/macOS).
"""
def clear_screen():
    sistema = platform.system()
    if(sistema == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

"""
Generic input handler that validates user selection against a list of allowed keys.
Returns the normalized lowercase selection.
"""
def validation_option(options):
    option = input().lower()
    while(option not in options):
        print("✖ invalid option")
        print("Please select another option: ", end="")
        option = input().lower()
    return option

# -- Display Menus --

"""Renders the main application dashboard."""
def menu():
    clear_screen()
    time.sleep(0.2)
    print("=" * 24)
    print(" " * 5, "TASK MANAGER")
    print("=" * 24)
    print("[1] Add Task")
    print("[2] List Tasks")
    print("[3] Complete Task")
    print("[4] Delete Task")
    print("")
    print("[E] Exit")
    print("-" * 24)
    print("Please select an option: ", end="")

"""
Displays the complete task list with status indicators and 
hierarchical descriptions for active tasks.
"""
def list_tasks_menu(tasks):
    clear_screen()
    time.sleep(0.2)
    print("=" * 24)
    print(" " * 5, "List Tasks")
    print("=" * 24)
    for task in tasks:
        print(f"- ", end="")
        if(task["pending"] == True):
            print("( ) ", end="")
        else:
            print("(✔) ", end="")
        print(f"{task['title']}")
        if task.get("description"):
            print(f"      └─ Description: {task['description']}")
    print("\n")
    print("[B] Back")
    print("[E] Exit")
    print("-" * 24)
    print("Please select an option: ", end="")

"""Displays only tasks eligible for completion (pending status)."""
def complete_task_menu(tasks):
    clear_screen()
    time.sleep(0.2)
    print("=" * 24)
    print(" " * 5, "List Tasks")
    print("=" * 24)
    for i in range(len(tasks)):
        if(tasks[i]["pending"] == True):
            print(f"[{i+1}] ( ) {tasks[i]['title']}")
    print("\n")
    print("[B] Back")
    print("[E] Exit")
    print("-" * 24)
    print("Please select an option: ", end="")

"""Displays all tasks with their corresponding index for removal selection."""
def delete_task_menu(tasks):
    clear_screen()
    time.sleep(0.2)
    print("=" * 24)
    print(" " * 5, "List Tasks")
    print("=" * 24)
    for i in range(len(tasks)):
        print(f"[{i+1}] ", end="")
        if(tasks[i]["pending"] == True):
            print("( ) ", end="")
        else:
            print("(✔) ", end="")
        print(f"{tasks[i]['title']}")
    print("\n")
    print("[B] Back")
    print("[E] Exit")
    print("-" * 24)
    print("Please select an option: ", end="")

# -- User Feedback --

"""Visual confirmation for successful task creation."""
def new_task_feedback():
    clear_screen()
    print("+ New tasks added!")
    time.sleep(1)
    clear_screen()

"""Visual confirmation for task status updates."""
def task_completed_feedback():
    clear_screen()
    print("✓ Task marked as completed!")
    time.sleep(1)
    clear_screen()

"""Visual confirmation for task deletion."""
def task_removed_feedback():
    clear_screen()
    print("🗑 Task successfully removed!")
    time.sleep(1)
    clear_screen()

"""Graceful exit message before program termination."""
def exit_feedback():
    clear_screen()
    print("Exiting the program... Goodbye!")
    time.sleep(1)
    clear_screen()

# -- Data Entry --

"""Prompts for task title and validates that it is not empty."""
def title_new_task():
    clear_screen()
    time.sleep(0.2)
    title = input("Title: ")
    while(title == ""):
        clear_screen()
        title = input("Title (required): ")
    return title

"""Collects an optional task description."""
def description_new_task():
    description = input("Description (optional): ")
    return description