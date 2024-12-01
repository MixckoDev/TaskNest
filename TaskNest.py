import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found. Add some!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['name']} (Priority: {task['priority']})")

def add_task(tasks):
    name = input("Task name: ").strip()
    priority = input("Priority (Low/Medium/High): ").strip().capitalize()
    if priority not in ["Low", "Medium", "High"]:
        print("Invalid priority! Defaulting to 'Low'.")
        priority = "Low"
    tasks.append({"name": name, "priority": priority, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def mark_task_completed(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    print("Welcome to TaskNest!")
    while True:
        print("\nMenu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Completed")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
