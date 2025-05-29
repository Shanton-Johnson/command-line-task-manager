import sys
import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📝 No tasks found.")
    else:
        print("✅ Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(task_desc):
    tasks = load_tasks()
    tasks.append(task_desc)
    save_tasks(tasks)
    print(f"➕ Added task: {task_desc}")

def remove_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"❌ Removed task: {removed}")
    else:
        print("⚠️ Invalid task number.")

def show_help():
    print("""
📖 Task Manager Commands:
    python task_manager.py list                 # List all tasks
    python task_manager.py add "Task description"  # Add a new task
    python task_manager.py remove <task_number>    # Remove a task by number
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    else:
        command = sys.argv[1]

        if command == 'list':
            list_tasks()
        elif command == 'add':
            if len(sys.argv) < 3:
                print("⚠️ Please provide a task description.")
            else:
                task_desc = ' '.join(sys.argv[2:])
                add_task(task_desc)
        elif command == 'remove':
            if len(sys.argv) < 3:
                print("⚠️ Please provide the task number to remove.")
            else:
                try:
                    task_number = int(sys.argv[2])
                    remove_task(task_number)
                except ValueError:
                    print("⚠️ Task number must be an integer.")
        else:
            show_help()
