# Class for MAKING A STUDENT
class MakeStudent:
    def __init__(self, name, id, grades = []):
        self.name = name
        self.id = id
        self.grades = grades

    def __str__(self):
        pass


# Class for MANAGING A MADE STUDENT (Add grade, calculate average, Display info, find by ID and/or name, get letter for average (A=90+, B=80-89, C=70-79, D=60-69, F=<60))
class GradeBook:
    def __init__(self, student):
        self.student = student