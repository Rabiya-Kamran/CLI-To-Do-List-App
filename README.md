# ToDo List Application
## Overview
This To-Do List application is a Python-based command-line tool that helps users manage their tasks efficiently. Users can add, delete, update, and view tasks, and the application saves the task list to a JSON file (ToDoFile.json) for persistence.

## Features
**Add Task:** Add a new task to the to-do list. Tasks are marked as "not done" by default.  
**Delete Task:** Remove an existing task from the list.  
**Update Task:** Mark a task as "done."  
**View Tasks:** Display all tasks in the to-do list, along with their statuses.  
**Save to File:** Automatically save tasks to the ToDoFile.json file when exiting the application.  

## Requirements
- Python 3.x
- JSON module (built-in with Python)

## How It Works
1. The program initializes by loading tasks from the JSON file (sample.json). If the file doesn't exist or contains invalid JSON, a new task list is created.
2. Users interact with the application through a menu-driven command-line interface.
3. All tasks and their statuses are stored in lowercase to ensure uniformity.
4. Changes are saved to the sample.json file upon exiting the application.

## File Structure
**sample.json:** A JSON file used to store tasks and their statuses. The file is updated when exiting the application.

## Usage
## Run the Application
Run the script using Python:

```python
python ToDo.py
```
# Menu Options
After running the program, you can choose one of the following options:

## 1. Add Task:

Enter the task you want to add.
- Example: Enter task to be added: Complete assignment
- Output: Task added in todo list and is marked as not done by default.
## 2. Delete Task:

- Enter the name of the task you want to delete.
- Example: Enter task to be deleted: Complete assignment
- Output:
    - If the task exists: Task deleted.
    - If the task doesn't exist: Task not present in todo list.
## 3. Update Task:

- Enter the name of the task you want to mark as "done."
- Example: Enter task to be updated: Complete assignment
- Output:
   - If the task exists: Task updated as done.
   - If the task doesn't exist: Task not present in todo list.
## 4. View Tasks:

Display all tasks and their statuses.
Example Output:
```python
All tasks in todo list are listed below:

complete assignment not done
read book done
```
## 5. Exit:

Save the current tasks to ToDoFile.json and exit the program.
Output: Thank you for using the ToDo app! Goodbye!

# Example JSON File
Here’s an example of how the sample.json file might look:
```python
{
    "complete assignment": "not done",
    "read book": "done"
}
```

# Error Handling
- If the sample.json file is missing, a new one is created automatically.
- If the file contains invalid JSON, the application initializes with an empty task list.
# Notes
- Tasks are case-insensitive. For example, adding "Read Book" or "read book" will be treated the same.
- Ensure that you exit the application properly (option 5) to save changes to the JSON file.
