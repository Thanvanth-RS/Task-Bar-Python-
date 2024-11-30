import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, title, due_date, priority):
    """Add a new task to the list."""
    task = {'title': title, 'due_date': due_date, 'priority': priority}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added.")


def delete_task(tasks, index):
    """Delete a task by index."""
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Invalid task index!")


def view_tasks(tasks):
    """View all tasks."""
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['title']} (Due: {task['due_date']}, Priority: {task['priority']})")
    else:
        print("No tasks available.")


def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High, Medium, Low): ")
            add_task(tasks, title, due_date, priority)
        elif choice == '2':
            view_tasks(tasks)
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option! Please try again.")


if __name__ == '__main__':
    main()
