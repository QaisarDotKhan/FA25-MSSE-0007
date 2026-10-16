def validate_marks(marks):
    try:
        numeric_marks = float(marks)
    except (ValueError, TypeError):
        return False
        
    if numeric_marks < 0 or numeric_marks > 100:
        return False
    return True