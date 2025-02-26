import json
with open('student.json', 'r') as file:
    data = json.load(file)

 # ...existing code...
with open('student.json', 'r') as file:
    data = json.load(file) # load the json data from the file

students = data['students']

for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Math Grade: {student['grades']['math']}")
    print(f"Science Grade: {student['grades']['science']}")
    print()
