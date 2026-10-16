# def main():
#     name = input("Enter student name: ")

#     # Validation
#     if name == "":
#         print("Invalid name")
#         return

#     # Calculation
#     marks = 80
#     bonus = 5
#     total_marks = marks + bonus

#     print(f"Student: {name}")
#     print(f"Total Marks: {total_marks}")
 
# if __name__ == "__main__":
#     main()

from Calculate import calculate_grade
from Validate import validate_name, validate_marks
from student import Student
from report import display_report

def main():
    name = input("Enter student name: ")

    validate_name(name)

    marks = int(input("Enter marks: "))

    validate_marks(marks)

    grade = calculate_grade(marks)

    student = Student(name, marks, grade)

    display_report(student)
 
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
 
if __name__ == "__main__":
    main()
