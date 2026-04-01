import csv
a_list = []
try:
    with open('docs/grade_book.csv', 'r') as file:
        content = csv.reader(file)
        headers = next(content)
        for line in content:
            a_list.append([line[0], line[1], line[2], line[3], line[4]])
            continue
        print("Lines appended")
except:
    print("Could not open file in ALL_CLASSES GRADEBOOK __INIT__ method")
