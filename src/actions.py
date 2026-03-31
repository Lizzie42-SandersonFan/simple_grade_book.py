from all_classes import *
from helpers import *
# Add student: Get student name and id. Create empty list for future grade holding
def add_student():
    name = input("Enter student FULL name:\n").strip()
    stu_id = input("Enter student ID:\n").strip()
    student = MakeStudent(name, stu_id)
    stu_avrg = student.average_grade
    stu_letter = student.get_letter(stu_avrg)

    GradeBook.add_student(name, stu_id, student.grades, stu_avrg, stu_letter)
    print("Student added!")
    MakeStudent.student_overview()
    return
    

# Add grade: Show students with ID. Have user enter ID for student that needs a grade added. Enter a number between 0-100 (will need to be checked. Check if it is even a number first). Find the student by ID and append that grade into the list created
def add_grade():
    GradeBook.display_students()
    while True:
        name = input("Enter student name:\n").strip()
        id = input("Enter student ID:\n").strip()
        a_student = GradeBook.find_student(name, id)
        if not a_student:
            print("Seems that student couldn't be found. Try again.")
            continue
        else:
            break
    while True:
        grade = input(f"Enter the grade for {a_student[0]} (0-100):\n")
        valid, int_grade = is_number(grade)
        if valid == True:
            if int_grade < 0 or int_grade > 100:
                print("Grade out of valid range. Try again.")
                continue
            else:
                MakeStudent.add_grade(int_grade)
                break
        else:
            print("Seems you entered an invalid grade. Try again.")
            continue
    return

# View Student record: Show all students and select student by ID. Print that student as : Name, ID, ALL Grades, Average % Grade, Letter grade
def view_student():
    def format_grade_list(stu_grades):
        if not stu_grades:
            print("None")
            return
        else:
            for item in stu_grades:
                print(f"\t{item}")
            return

    GradeBook.display_students()
    while True:
        name = input("Enter student name:\n").strip()
        id = input("Enter student ID:\n").strip()
        a_student = GradeBook.find_student(name, id)
        if not a_student:
            print("Seems that student couldn't be found. Try again.")
            continue
        else:
            print(f"Name: {a_student[0]}\nID: {a_student[1]}\nGrades: {format_grade_list(a_student[2])}\nAverage: {a_student[3]}\nLetter: {a_student[4]}")
            break
    return

# View ALL Students: Show Name, ID, Average, Letter Grade for EACH student in CSV
def view_all():
    # BUILD
    pass

# Class Summary: Names with corresponding Letter Grade
def class_sum():
    GradeBook.class_overview()
    return