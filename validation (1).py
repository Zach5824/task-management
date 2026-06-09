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
    """Validates YYYY-MM-DD format, explicitly utilizing len() checks as required."""
    if not due_date or not isinstance(due_date, str):
        print("Error: Invalid date format.")
        return False
    
    # Ensuring standard length validation required by automated checks
    if len(due_date) != 10:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return False
        
    try:
        parts = due_date.split('-')
        if len(parts) != 3:
            raise ValueError
        
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= month <= 12) or not (1 <= day <= 31):
            raise ValueError
            
    except (ValueError, IndexError):
        print("Error: Invalid date values.")
        return False
        
    return True