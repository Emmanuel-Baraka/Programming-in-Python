from abc import ABC, abstractmethod

# Parent Class (Base Class)
class Employee(ABC):
    def __init__(self, name, salary):
        # Private attributes demonstrate Encapsulation
        self.__name = name
        self.__salary = salary

    def display_info(self):
        return f"Employee Name: {self.__name}"

    @abstractmethod
    def calculate_salary(self):
        # Abstract method demonstrates Abstraction
        pass

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

# Child Classes demonstrate Inheritance
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        # Polymorphism: Implementation for Full Time
        return self.get_salary()

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        # Polymorphism: Implementation for Part Time (50%)
        return self.get_salary() * 0.5

# --- Program Execution (Part d) ---

# Create objects
emp1 = FullTimeEmployee("Alice", 60000)
emp2 = PartTimeEmployee("Bob", 40000)

# Store them in a list
employee_list = [emp1, emp2]

# Loop to call methods for each object
for emp in employee_list:
    print(emp.display_info())
    print(f"Calculated Salary: {emp.calculate_salary()}")
    print("-" * 25)
