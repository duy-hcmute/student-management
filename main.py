class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

students = []

def add_student():
    id = input("ID: ")
    name = input("Name: ")
    students.append(Student(id, name))
    print("Added!")

def show_students():
    for s in students:
        print(s.id, "-", s.name)

add_student()
show_students()
