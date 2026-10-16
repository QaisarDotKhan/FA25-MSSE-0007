def display_report(student_obj) -> str:
    return (
        f"\n--- Student Report: {student_obj.name} ---\n"
        f"ID: {student_obj.id}\n"
        f"Program: {student_obj.program}\n"
        f"Semester: {student_obj.semester}\n"
        f"Marks: {student_obj.marks}\n"
        f"Final Grade: {student_obj.grade}\n"
        f"-----------------------------------------"
    )