from src.student_app.services.calculate import calculate_grade

def test_grade_boundaries():
    assert calculate_grade(85) == "A"
    assert calculate_grade(75) == "B"
    assert calculate_grade(65) == "C"
    assert calculate_grade(55) == "D"
    assert calculate_grade(40) == "F"