from src.student_app.utils.validate import validate_marks

def test_valid_marks():
    assert validate_marks(85) is True
    assert validate_marks(0) is True
    assert validate_marks(100) is True

def test_invalid_marks():
    assert validate_marks(-5) is False
    assert validate_marks(105) is False
    assert validate_marks("invalid_number") is False