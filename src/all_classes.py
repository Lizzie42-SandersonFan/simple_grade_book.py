# Class for MAKING A STUDENT
from helpers import *

# (Add grade, calculate average, Display info, get letter for average (A=90+, B=80-89, C=70-79, D=60-69, F=<60))
class MakeStudent:
    def __init__(self, name, id, grades = []):
        self.name = name
        self.id = id
        self.grades = grades

    def student_overview(self):
        if not self.grades:
            # The list is empy and I want to display that fact
            grade_display = "None"
        else:
            # There are grades to display
            grade_display = self.grades # Set to the list so the list is printed

        return f"Name: {self.name}, ID: {self.id}, Grades: {grade_display}"

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        avg = 0
        for item in self.grades:
            avg += item
        avg = avg / len(self.grades)
        avg = round(avg, 2)
        return avg
    
    def get_letter(average):
        if average >= 90:
            letter = "A"
        elif average >= 80 and average < 90:
            letter = "B"
        elif average >= 70 and average < 80:
            letter = "C"
        elif average >= 60 and average < 70:
            letter = "D"
        else:
            letter = "F"
        
        return letter


# Class for MANAGING LOTS OF STUDENTS. Add student, find student, see class overview, see all students for selection
class GradeBook:
    def __init__(self, students =[]):
        self.students = students

    def display_students(self):
        for child in self.students:
            print(f"Name: {child[0]}(ID: {child[1]})")

    def add_student(self, name, id, grades, average, letter):
        self.students.append([name, id, grades, average, letter])

    def find_student(self, name, id):
        for student in self.students:
            if student['name'] == name or student['id'] == id:
                return student
            else:
                continue

    def class_overview(self):
        for kid in self.students:
            # Print the name (0 in list) and the LETTER grade (posision 4)
            print(f"Name: {kid[0]}, Grade: kid[4]")