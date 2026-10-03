# Student Management System

## 1. Project Description

The Student Management System is a simple Python console application used to manage student records.
The system allows the user to add, display, search, update, and delete student records. It can also calculate the average marks of a student and save the student records in a CSV file.
This project demonstrates important Object-Oriented Programming concepts in Python.

## 2. Objectives

The main objectives of this project are:
- To manage student records easily.
- To add and display student information.
- To search for a student using the roll number.
- To update student marks.
- To delete student records.
- To calculate average marks.
- To store student information in a CSV file.
- To demonstrate OOP concepts in Python.

## 3. Technologies Used
- Python
- Visual Studio Code
- CSV File Handling
- Object-Oriented Programming

## 4. Main Features
The project provides the following features:
1. Add Student
2. Display Students
3. Search Student
4. Update Marks
5. Delete Student
6. Calculate Average
7. Save Records
8. Exit

## 5. Classes Used
### Person
`Person` is an abstract base class.
It stores the name of a person and contains the abstract `display()` method.

### Student
`Student` is derived from the `Person` class.
It stores:
- Roll Number
- Name
- Marks
It also calculates the average marks of the student.

### FileManager
`FileManager` is used to save student records into a CSV file.

### Student Management
The main program manages the student records and provides different operations such as adding, searching, updating, and deleting students.

## 6. OOP Concepts Used
### Classes and Objects
The project uses classes and objects to represent students and manage student information.
### Encapsulation
Student information is stored using private attributes. Getter and setter methods are used to access and modify the data
### Inheritance
The `Student` class inherits from the `Person` class.
### Abstraction
The `Person` class is an abstract class using Python's `abc` module.
### File Handling
Student records are saved in a CSV file named `students.csv`.
### Exception Handling
The program handles invalid input using exception handling.
## 7. How the Project Works
When the program starts, it displays a menu.
The user can select an option from the menu.
For example:
- Select `1` to add a student.
- Select `2` to display students.
- Select `3` to search for a student.
- Select `4` to update marks.
- Select `5` to delete a student.
- Select `6` to calculate average marks.
- Select `7` to save records.
- Select `8` to exit.

## 8. How to Run the Project
### Step 1
Install Python on the computer.
### Step 2
Open the project folder in Visual Studio Code.
### Step 3
Open the VS Code terminal.
### Step 4
Run the following command:
    python student_management.py
### Step 5
The Student Management System menu will appear.
### Step 6
Select an option and follow the instructions displayed on the screen.

## 9. Project Files
The project contains the following files:
    Student_Management/
    |
    |-- student_management.py
    |-- students.csv
    |-- README.md
    |
    |-- screenshot/
        |-- add_student.png

### student_management.py
Contains the main Python source code.
### students.csv
Stores the student records.
### README.md
Contains information about the project and instructions for running it.
### screenshot
Contains screenshots of the important operations of the project.

## 10. Sample Operations
The following operations are implemented:
- Adding a student
- Displaying student records
- Searching for a student
- Updating marks
- Deleting a student
- Calculating average marks
- Saving student records

## 11. Conclusion
The Student Management System is a simple Python application for managing student information.
The project demonstrates Object-Oriented Programming concepts such as classes, objects, encapsulation, inheritance, and abstraction. It also demonstrates file handling and exception handling.
The project provides a simple and easy-to-use console interface for managing student records.