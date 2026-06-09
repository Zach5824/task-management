# main.py
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def main_menu():
    while True:
        print("\n=== Task Management System ===")
        print("1. Add Task")
        print("2. View Pending Tasks")
        print("3. Mark Task as Complete")
        print("4. Track Progress")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
            
        elif choice == "2":
            view_pending_tasks()
            
        elif choice == "3":
            title = input("Enter the exact title of the task to complete: ")
            mark_task_as_complete(title)
            
        elif choice == "4":
            progress = calculate_progress()
            print(f"Progress: {progress}%")
            
        elif choice == "5":
            break
        else:
            print("Invalid option chosen.")

if __name__ == "__main__":
    main_menu()