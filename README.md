# ToDo List Application
## Overview
This To-Do List application is a Python-based command-line tool that helps users manage their tasks efficiently. Users can add, delete, update, and view tasks, and the application saves the task list to a JSON file (sample.json) for persistence.

## Features
**Add Task:** Add a new task to the to-do list. Tasks are marked as "not done" by default.
**Delete Task:** Remove an existing task from the list.
**Update Task:** Mark a task as "done."
**View Tasks:** Display all tasks in the to-do list, along with their statuses.
**Save to File:** Automatically save tasks to the sample.json file when exiting the application.

## Requirements
- Python 3.x
- JSON module (built-in with Python)
## How It Works
1. The program initializes by loading tasks from the JSON file (sample.json). If the file doesn't exist or contains invalid JSON, a new task list is created.
2. Users interact with the application through a menu-driven command-line interface.
3. All tasks and their statuses are stored in lowercase to ensure uniformity.
4. Changes are saved to the sample.json file upon exiting the application.
