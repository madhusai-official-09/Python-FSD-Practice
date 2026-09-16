# 1. Create a class Employee with attributes name and salary. 
# Create a child class Manager that inherits from Employee and adds department. 
# Display all three details using the child object. 
# Input: Name: Ravi Salary: 45000 Department: IT 
# Output: Name: Ravi Salary: 45000 Department: IT

""" class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        
class Manger(Employee):
    def __init__(self, name, salary,depart):
        super().__init__(name, salary)
        self.department = depart
        
    def display(self):
        super().display()
        print(f"Department: {self.department}")
        
emp1 = Manger("Ravi", 45000, "IT")
emp1.display() """

# 2. Create a parent class Mobile with a method power_on() that prints "Mobile Powered On". 
# Create a child class SmartPhone with a method use_app() that prints "Using Instagram". 
# Create a SmartPhone object and call both methods. 
# Output: Mobile Powered On Using

""" class Mobile:
    def power_on(self):
        print("Mobile Powered On")

class SmartPhone(Mobile):
    def use_app(self):
        print("Using Instagram")
        
sm1 = SmartPhone()
sm1.power_on()
sm1.use_app() """

# 3. Create three classes: Student, Marks, and Result. Student stores the student's name. Marks inherits Student and stores marks. Result inherits Marks and displays the name, marks, and "Pass" if marks are 40 or above. 
# Input: Name: Anil Marks: 75 
# Output: Name

""" class Student:
    def __init__(self,name):
        self.name = name
        
class Marks(Student):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks = marks
        
class Result(Marks):
    def __init__(self,name, marks):
        super().__init__(name,marks)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        if self.marks>=40:
            print("PASS")
        else:
            print("FAIL")
            
st1 = Result("Ravi", 75)
st1.display() """

# 4. Create a parent class Company with a method company_name() that prints "ABC Technologies". Create two child classes Developer and Tester, each having their own method to display their role. Create objects of both child classes and display the company name

""" class Company:
    def company_method(self):
        print("ABC Technologies")
        
class Developer(Company):
    def display(self):
        print("Role: Developer")

class Tester(Company):
    def display(self):
        print("Role: Tester")
        
dev1 = Developer()
dev1.company_method()
dev1.display()

dev2 = Tester()
dev2.company_method()
dev2.display() """

# 5. Create a parent class Payment with a method pay() that prints "Payment Processing". Create a child class UPIPayment that overrides the pay() method and prints "Paid using UPI". Create an object of UPIPayment and call pay(). Output: Paid using UPI

""" class Payment:
    def pay(self):
        print("Payment Processing.")
        
class UPIPayment(Payment):
    def pay(self):
        print("Paid using UPI")
            
obj1 = UPIPayment()
obj1.pay() """       


