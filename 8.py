"""

#question
Write a Python program to create a class named Person with attributes name, age and
gender. Implement methods to greet and introduce the person. Also, implement multiple
inheritance by creating two subclasses named Student and Teacher that inherit from
Person and have additional attributes like course and subject respectively.

"""

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hello, my name is {self.name}."

    def introduce(self):
        return f"I am {self.name}, {self.age} years old, and I am {self.gender}."

class Student(Person):
    def __init__(self, name, age, gender, course):
        super().__init__(name, age, gender)
        self.course = course

    def introduce(self):
        person_intro = super().introduce()
        return f"{person_intro} I am a student in the {self.course} program."

class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def introduce(self):
        person_intro = super().introduce()
        return f"{person_intro} I am a {self.subject} teacher."

person1 = Person("Alice", 30, "female")
student1 = Student("Bob", 20, "male", "Computer Science")
teacher1 = Teacher("Eve", 35, "female", "Math")

print(person1.greet())
print(person1.introduce())

print(student1.greet())
print(student1.introduce())

print(teacher1.greet())
print(teacher1.introduce())
