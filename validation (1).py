# task_manager/validation.py

def validate_task_title(title):
    """Validates that the title is not empty and is a string."""
    if not title or not isinstance(title, str) or title.strip() == "":
        print("Error: Title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    """Validates that the description is a string."""
    if not isinstance(description, str):
        print("Error: Description must be text.")
        return False
    return True

def validate_due_date(due_date):
    """Validates simple YYYY-MM-DD format length and presence."""
    if not due_date or len(due_date) != 10 or due_date[4] != '-' or due_date[7] != '-':
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return False
    return True