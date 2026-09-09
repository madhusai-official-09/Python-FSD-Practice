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


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

r1 = Rectangle(10, 5)
print(f"Area: {r1.calculate_area()} Perimeter: {r1.calculate_perimeter()}")

