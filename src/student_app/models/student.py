class Student:
    def __init__(self, student_id: str, name: str, program: str, semester: int, marks: float):
        self.id = student_id
        self.name = name
        self.program = program
        self.semester = semester
        self.marks = marks
        self.grade = None