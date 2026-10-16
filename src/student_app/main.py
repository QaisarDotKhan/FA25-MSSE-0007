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

# from Services.Calculate import calculate_grade
# from utils.Validate import validate_name, validate_marks
# from models.student import Student
# from reports.student_report import display_report

# def main():
#     name = input("Enter student name: ")

#     validate_name(name)

#     marks = int(input("Enter marks: "))

#     validate_marks(marks)

#     grade = calculate_grade(marks)

#     student = Student(name, marks, grade)

#     display_report(student)
 
#     print(f"Marks: {marks}")
#     print(f"Grade: {grade}")
 
# if __name__ == "__main__":
#     main()




import json
import os
import sys

# Ensure src/ is on the system path for seamless module tracking
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from student_app.config import APP_NAME, DEBUG, MAX_STUDENTS
from student_app.logger import logger
from student_app.models.student import Student
from student_app.utils.validate import validate_marks
from student_app.services.calculate import calculate_grade
from student_app.reports.student_report import display_report

def main():
    logger.info(f"Starting {APP_NAME}...")
    if DEBUG:
        logger.info(f"Debug: {MAX_STUDENTS}")

    json_path = os.path.join("data", "student.json")
    
    # Exception Handling for File & Parsing Issues
    try:
        with open(json_path, "r") as file:
            data = json.load(file)
            logger.info("Successfully read student data record file.")
    except FileNotFoundError:
        logger.error(f"Missing file target at {json_path}")
        return
    except json.JSONDecodeError:
        logger.error("Corrupt or invalid JSON.")
        return

    # Business Validation
    if not validate_marks(data.get("marks")):
        logger.warning(f"Found out-of-bounds marks ({data.get('marks')}).")
        print("Invalid student record.")
        return

    # Process models
    student = Student(
        student_id=data["id"],
        name=data["name"],
        program=data["program"],
        semester=data["semester"],
        marks=float(data["marks"])
    )
    
    student.grade = calculate_grade(student.marks)
    logger.info("Grades successfully calculated.")

    # Output details
    print(display_report(student))
    logger.info("Application executed successfully and gracefully exited.")

if __name__ == "__main__":
    main()
