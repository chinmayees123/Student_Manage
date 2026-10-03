import csv
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    @abstractmethod
    def display(self):
        pass
class Student(Person):
    def __init__(self, roll_no, name, marks):
        super().__init__(name)
        self.__roll_no = roll_no
        self.__marks = marks
    def get_roll_no(self):
        return self.__roll_no
    def get_marks(self):
        return self.__marks
    def set_marks(self, marks):
        self.__marks = marks
    def average(self):
        return sum(self.__marks) / len(self.__marks)
    def display(self):
        print("\nRoll No:", self.__roll_no)
        print("Name:", self.get_name())
        print("Marks:", self.__marks)
        print("Average:", round(self.average(), 2))
class FileManager:
    def save(self, students):
        try:
            with open("students.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Roll No", "Name", "Marks"])
                for student in students:
                    writer.writerow([
                        student.get_roll_no(),
                        student.get_name(),
                        student.get_marks()
                    ])
            print("Records saved successfully.")
        except Exception:
            print("Error while saving file.")
students = []
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Calculate Average")
    print("7. Save Records")
    print("8. Exit")
    choice = input("Enter your choice: ")
    try:
        if choice == "1":
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            m1 = int(input("Enter Mark 1: "))
            m2 = int(input("Enter Mark 2: "))
            m3 = int(input("Enter Mark 3: "))
            student = Student(
                roll,
                name,
                [m1, m2, m3]
            )
            students.append(student)
            print("Student added successfully.")
        elif choice == "2":
            if len(students) == 0:
                print("No students found.")
            for student in students:
                student.display()
        elif choice == "3":
            roll = input("Enter Roll No to search: ")
            found = False
            for student in students:
                if student.get_roll_no() == roll:
                    student.display()
                    found = True
            if not found:
                print("Student not found.")
        elif choice == "4":
            roll = input("Enter Roll No: ")
            for student in students:
                if student.get_roll_no() == roll:
                    marks = int(
                        input("Enter new average mark: ")
                    )
                    student.set_marks(
                        [marks, marks, marks]
                    )
                    print("Marks updated.")
                    break
            else:
                print("Student not found.")
        elif choice == "5":
            roll = input("Enter Roll No to delete: ")
            for student in students:
                if student.get_roll_no() == roll:
                    students.remove(student)
                    print("Student deleted.")
                    break
            else:
                print("Student not found.")
        elif choice == "6":
            roll = input("Enter Roll No: ")
            for student in students:
                if student.get_roll_no() == roll:
                    print(
                        "Average:",
                        round(student.average(), 2)
                    )
                    break
            else:
                print("Student not found.")
        elif choice == "7":
            file_manager = FileManager()
            file_manager.save(students)
        elif choice == "8":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter valid numbers.")