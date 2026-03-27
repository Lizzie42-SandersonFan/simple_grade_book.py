# Class for MAKING A STUDENT
from helpers import *

class MakeStudent:
    def __init__(self, name, id, grades = []):
        self.name = name
        self.id = id
        self.grades = grades

    def __str__(self):
        if not self.grades:
            # The list is empy and I want to display that fact
            grade_display = "None"
        else:
            # There are grades to display
            grade_display = self.grades # Set to the list so the list is printed

        return f"Name: {self.name}, ID: {self.id}, Grades: {grade_display}"


# Class for MANAGING A MADE STUDENT (Add grade, calculate average, Display info, find by ID and/or name, get letter for average (A=90+, B=80-89, C=70-79, D=60-69, F=<60))
class GradeBook:
    def __init__(self, student):
        self.student = student

    def add_grade(self, student):
        self.student = student
        pass

    def find_average(self, student):
        self.student = student
        pass

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