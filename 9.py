"""

#question
Write a Python program to create a class named Calculator with methods for basic
arithmetic operations like add, subtract, multiply, and divide. Also, implement operator
overloading by defining special methods like add, sub, mul and truediv for the
Calculator class.

"""


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero."
        return x / y

    def __add__(self, other):
        return self.add(self, other)

    def __sub__(self, other):
        return self.subtract(self, other)

    def __mul__(self, other):
        return self.multiply(self, other)

    def __truediv__(self, other):
        return self.divide(self, other)

calc = Calculator()

print("Using methods for arithmetic operations:")
print("Add:", calc.add(5, 3))
print("Subtract:", calc.subtract(10, 4))
print("Multiply:", calc.multiply(7, 2))
print("Divide:", calc.divide(20, 5))

print("\nUsing operator overloading:")
print("Add:", calc + 5)
print("Subtract:", calc - 2)
print("Multiply:", calc * 3)
print("Divide:", calc / 2)
