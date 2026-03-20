# Task Manager (CLI)

## A modular Python-based task management application designed for the terminal. This project demonstrates clean code principles, data persistence, and a modular architecture.

## Key Features

* **modular architecture:** Implementation of the **"Separation of Concerns"** principle by distributing responsibilities across specialized modules to improve maintainability.
* **Data Persistence:** Robust local storage using **JSON files**, ensuring data integrity across different application sessions.
* **Cross-Platform:**  Automatic operating system detection (Windows/Unix) for optimized terminal screen management and a consistent user experience.

## technologies
* Python 3.10+ 
* JSON (Data Serialization)
* OS Module (System Calls)  

## Project Structure

* `main.py`: Application entry point. Orchestrates the interaction between UI, logic, and JSON storage modules.

* `interface.py`: Handles the visual part of the program, including menus and user feedback.

* `storage.py`: Manages data persistence, handling the reading and writing of the JSON file.

* `logic.py`: Processes the information and defines the main functions that make the program work.

