"""

#question
Write a Python program to create a class named Car with attributes model, color and
price. Implement methods to start, stop, and accelerate the car. Also, implement a static
method to count the number of cars created.

"""


class Car:
    total_cars = 0

    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        self.is_running = False
        Car.total_cars += 1

    def start(self):
        if not self.is_running:
            self.is_running = True
            return f"The {self.color} {self.model} is now running."
        else:
            return f"The {self.color} {self.model} is already running."

    def stop(self):
        if self.is_running:
            self.is_running = False
            return f"The {self.color} {self.model} has been stopped."
        else:
            return f"The {self.color} {self.model} is already stopped."

    def accelerate(self):
        if self.is_running:
            return f"The {self.color} {self.model} is accelerating."
        else:
            return f"The {self.color} {self.model} cannot accelerate when stopped."

    @staticmethod
    def count_cars():
        return f"Total cars created: {Car.total_cars}"

car1 = Car("Toyota Camry", "Blue", 25000)
car2 = Car("Ford Mustang", "Red", 40000)

print(car1.start())
print(car2.start())
print(car1.accelerate())
print(car2.accelerate())
print(car1.stop())
print(car2.stop())

print(Car.count_cars())
