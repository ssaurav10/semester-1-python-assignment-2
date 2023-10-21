"""

#question
Write a Python program to create a class named Student with attributes name, age and
grade. Implement a method to display the student’s information in a formatted string

"""


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}"

student1 = Student("John Smith", 18, "A")
student2 = Student("Jane Doe", 17, "B")

print("Student 1 Information:")
print(student1.display_info())

print("\nStudent 2 Information:")
print(student2.display_info())
