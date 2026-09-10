# 1. Create a class Student with the attributes name, roll_no, and marks. Create an object and display all the student details. 
# Input: name = "Rahul" roll_no = 101 marks = 85 
# Output: Name: Rahul Roll No: 101 Marks: 85

""" class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name} Roll No: {self.roll_no} Marks: {self.marks}")
        
s1 = Student("Rahul", 101, 85)
s1.display_details() """

# 2. Create a class Rectangle with attributes length and breadth. Create an object and calculate and display the area and perimeter of the rectangle. 
# Input: length = 10 breadth = 5 
# Output: Area: 50 Perimeter: 30

""" class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

r1 = Rectangle(10, 5)
print(f"Area: {r1.calculate_area()} Perimeter: {r1.calculate_perimeter()}") """

# 3. Create a class Employee with attributes name, employee_id, and salary. Create an object and display the employee details. Also calculate the salary after adding a ₹5000 bonus. 
# Input: name = "Arjun" employee_id = 101 salary = 30000 
# Output: Name: Arjun Employee ID: 101 Salary: 30000 Updated Salary: 35000

class Employee:
    def __init__(self,name,emply_id,salary):
        self.name = name
        self.emply_id=emply_id
        self.salary = salary
    def bonus(self):
        org_salary = self.salary+5000
        return org_salary
    def display(self):
        print(self.name)
        print(self.emply_id)
        print(self.bonus())
        
employee1=Employee("Arjun",101,30000)
employee1.bonus()
employee1.display()

# 4. Create a class Mobile with attributes brand, model, and price. Create an object and display the mobile details. 
# Input: brand = "Samsung" model = "A55" price = 30000 
# Output: Brand: Samsung Model: A55 Price: 30000