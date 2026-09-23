# 1. What is abstraction in Python? Explain how abstract classes and abstract methods are used, with a real-life example.
""" The abstraction is a fundamental concept in object-oriented programming (OOP) that allows you to hide the complex implementation details of a class and expose only the essential features to the user. """

# 2. What is polymorphism in Python? Explain method overriding with a suitable 
# example

""" The polymorphism is a concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). """ 

# 3. What is method overriding? Explain how it is related to polymorphism with a simple example. 

""" The method overriding is a feature in object-oriented programming that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. """

""" class Animal:
    def sound(self):
        print("Animal Sound.")
class Dog:
    def sound(self):
        print("Dog Barks.")
class Cat:
    def sound(self):
        print("Cat Meows.")
        
animals = [Dog(),Cat()]
for animal in animals:
    animal.sound() """

# 4. Create an abstract class Employee with an abstract method calculate_salary(). Create two child classes, FullTimeEmployee and PartTimeEmployee, that implement the method differently. 
#  Full-time employee salary = monthly salary. 
#  Part-time employee salary = hours worked × hourly rate. 

""" from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FulltimeEmployee(Employee):
    def __init__(self,monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self,hours_worked,hours_rate):
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate

    def calculate_salary(self):
        return self.hours_worked * self.hours_rate

full_time  = FulltimeEmployee(5000)
part_time = PartTimeEmployee(40, 20) 
print("Full-time Employee Salary:", full_time.calculate_salary())
print("Part-time Employee Salary:", part_time.calculate_salary()) """

# 5. Company Payment System 
# A company has different payment methods. Create an abstract class Payment with pay(). 
# Create UPI and CreditCard classes that override pay(). 
# Use Abstraction, Inheritance, Encapsulation, and Polymorphism. 
# Input: 
# Ravi UPI 
# Anil CreditCard 
# Output: 
# Ravi paid using UPI 
# Anil paid using Credit Card

""" from abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    @abstractmethod
    def pay(self):
        pass
    
class UPI(Payment):
    def pay(self):
        print(f"{self.get_name()} paid using UPI")
class CreditCard(Payment):
    def pay(self):
        print(f"{self.get_name()} paid using Credit Card")
ravi = UPI("Ravi")
anil = CreditCard("Anil")
ravi.pay()
anil.pay() """