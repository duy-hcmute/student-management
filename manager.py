    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            self.save_to_file()
            return True
        return False
import csv
import os
from student import Student


class StudentManager:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    self.students.append(Student(row[0], row[1], row[2]))

    def save_to_file(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for s in self.students:
                writer.writerow(s.to_list())

    def add_student(self, student_id, name, year):
        self.students.append(Student(student_id, name, year))
        self.save_to_file()

    def show_students(self):
        if not self.students:
            print("No students found.")
            return
        for s in self.students:
            print(s)
