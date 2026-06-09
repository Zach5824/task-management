# task_manager/task_utils.py
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# This list will hold our task dictionaries
tasks_list = []

def add_task(title, description, due_date):
    """Validates and adds a new task to the collection."""
    if (validate_task_title(title) and 
        validate_task_description(description) and 
        validate_due_date(due_date)):
        
        new_task = {
            "title": title.strip(),
            "description": description.strip(),
            "due_date": due_date.strip(),
            "completed": False
        }
        tasks_list.append(new_task)
        print(f"Task '{title}' added successfully!")
        return True
    else:
        print("Failed to add task due to validation errors.")
        return False

def mark_task_as_complete(title):
    """Finds a pending task by title and marks it complete."""
    for task in tasks_list:
        if task["title"].lower() == title.strip().lower():
            if task["completed"]:
                print(f"Task '{task['title']}' is already marked as complete.")
                return
            task["completed"] = True
            print(f"Task '{task['title']}' marked as complete!")
            return
    print(f"Task '{title}' not found.")

def view_pending_tasks():
    """Displays all tasks where completed is False."""
    pending = [t for t in tasks_list if not t["completed"]]
    if not pending:
        print("\nNo pending tasks found!")
        return
    
    print("\n--- Pending Tasks ---")
    for i, task in enumerate(pending, 1):
        print(f"{i}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")
        print("-" * 20)

def calculate_progress():
    """Calculates and prints the percentage of tasks completed."""
    total_tasks = len(tasks_list)
    if total_tasks == 0:
        print("\nProgress: No tasks available to track. (0%)")
        return
    
    completed_tasks = len([t for t in tasks_list if t["completed"]])
    percentage = (completed_tasks / total_tasks) * 100
    print(f"\nProgress: {completed_tasks}/{total_tasks} tasks completed ({percentage:.1f}%)")