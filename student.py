class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age}"


students = []

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    students.append(Student(student_id, name, age))


def show_students():
    if not students:
        print("Student list is empty.")
    for s in students:
        print(s)


def main():
    while True:
        print("\n1. Add student")
        print("2. Show students")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
