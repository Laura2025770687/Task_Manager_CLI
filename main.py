"""Application entry point: Orchestrates the workflow between Interface, Logic, and Storage modules."""

import storage as st
import interface as ui
import logic as lg

import sys

#-- Sub-menu Handlers --

"""Manages the task listing view and navigation."""
def list_tasks(tasks):

    while True:
        ui.list_tasks_menu(tasks)

        option = ui.validation_option(["b", "e"])

        match option:
            case "b":
                break
            case "e":
                ui.exit_feedback()
                sys.exit()

"""Coordinates the task completion process between UI, Logic, and Storage."""
def complete_tasks(tasks, last_id):
    
    while True:
        ui.complete_task_menu(tasks)

        options = lg.options_validation_complete_task(tasks)
        option = ui.validation_option(options)

        match option:
            case "b":
                break
            case "e":
                ui.exit_feedback()
                sys.exit()
            case _:
                lg.mark_task_as_complete(tasks, option)
                st.save_tasks_archive(tasks, last_id)
                ui.task_completed_feedback()

"""Handles the task deletion flow and updates data persistence."""
def delete_task(tasks, last_id):
    while True:

        ui.delete_task_menu(tasks)

        options = lg.options_validation_delete_task(tasks)
        option = ui.validation_option(options)

        match option:
            case "b":
                break
            case "e":
                ui.exit_feedback()
                sys.exit()
            case _:
                lg.remove_task(tasks, option)
                st.save_tasks_archive(tasks, last_id)
                ui.task_removed_feedback()
    
#-- Main Execution --

"""Main application loop and top-level menu navigation."""
def main():
    data = st.open_tasks_archive()
    tasks = data["tasks"]
    last_id = data["last_id"]

    while True:
    
        ui.menu()
        option = ui.validation_option(["1", "2", "3", "4", "e"])

        match option:
            case "1":

                title = ui.title_new_task()
                description = ui.description_new_task()
                last_id = lg.add_task(tasks,last_id, title, description)
                st.save_tasks_archive(tasks, last_id)
                ui.new_task_feedback()

            case "2":
                list_tasks(tasks)
            case "3":
                complete_tasks(tasks, last_id)
            case "4":
                delete_task(tasks, last_id)
            case "e":
                ui.exit_feedback()
                sys.exit()

if __name__ == "__main__":
    main()