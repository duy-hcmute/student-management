from manager import StudentManager


def main():
    manager = StudentManager()

    while True:
        print("\n=== STUDENT MANAGEMENT ===")
        print("1. Add student")
        print("2. Show all students")
        print("3. Find student by ID")
        print("4. Delete student by ID")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            year = input("Year: ")
            manager.add_student(sid, name, year)
            print("Student added!")

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            sid = input("Enter student ID to find: ")
            student = manager.find_student(sid)
            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == "4":
            sid = input("Enter student ID to delete: ")
            if manager.delete_student(sid):
                print("Student deleted.")
            else:
                print("Student not found.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
