"""

#question
Write a Python program to create a class named Employee with attributes name, id, and
salary. Implement methods to get and set the salary of the employee. Also, implement a
class method to calculate the average salary of all employees.

"""

class Employee:
    all_employees = []

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        Employee.all_employees.append(self)

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.salary = new_salary
            return f"Salary for {self.name} (ID: {self.id}) set to ${self.salary}."
        else:
            return "Invalid salary amount. Salary must be non-negative."

    @classmethod
    def calculate_average_salary(cls):
        total_salary = sum(employee.salary for employee in cls.all_employees)
        average_salary = total_salary / len(cls.all_employees)
        return average_salary

employee1 = Employee("John Doe", 1, 50000)
employee2 = Employee("Jane Smith", 2, 60000)
employee3 = Employee("Bob Johnson", 3, 55000)

print("Employee 1 Salary:", employee1.get_salary())
print("Employee 2 Salary:", employee2.get_salary())

print(employee1.set_salary(55000))
print(employee2.set_salary(62000))

average_salary = Employee.calculate_average_salary()
print(f"Average Salary of All Employees: ${average_salary}")
