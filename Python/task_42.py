# 1. Create a Vehicle class with a method start() that prints "Vehicle is starting". Create a Car class that inherits from Vehicle and overrides start() to print "Car starts with a key". Create a Car object and call start(). Expected Output: Car starts with a key.

""" class Vehicle:
    def start(self):
        print("Vehicle is starting")
        
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
        
c1 = Car()
c1.start() """

# 2. Create Dog and Cat classes. Both classes should have a method sound(). Dog.sound() should print "Dog barks" Cat.sound() should print "Cat meows" Create objects of both classes and call sound() using the same variable name one after another. Expected Outpu

""" class Dog:
    def sound(self):
        print("Dog barks")
    
class Cat:
    def sound(self):
        print("Cat meows")

obj = [Dog(), Cat()]
for i in obj:
    i.sound() """
    
# 3. Create Bike and Car classes with a method move(). Bike.move() → "Bike moves on two wheels" Car.move() → "Car moves on four wheels" Create a function show_movement(vehicle) that calls vehicle.move(). Pass both objects to the function. Expected Output: Bike

""" class Bike:
    def move(self):
        print("Bike moves on two wheels")
    
class Car:
    def move(self):
        print("Car moves on four wheels")

def show_movement(vehicle):
    vehicle.move()
    
show_movement(Bike())
show_movement(Car()) """

# 4. Create a parent class Employee with a method salary() that prints "Basic Salary". Create two child classes: Developer → salary() prints "Developer Salary: 50000" Tester → salary() prints "Tester Salary: 40000" Create objects of both child classes and call

""" class Employee:
    def salary(self):
        print("Basic Salary.")
        
class Developer(Employee):
    def salary(self):
        print("Developer Salary: 50000")
        
class Tester(Employee):
    def salary(self):
        print("Tester Salary: 40000")
dev = Developer()
dev.salary()
tes = Tester()
tes.salary() """

# 5. Create a parent class Shape with a method area() that prints "Area of Shape". Create Circle and Rectangle classes that inherit from Shape. Circle.area() → print "Circle Area" Rectangle.area() → print "Rectangle Area" Store both objects in a list and use a

""" class Shape:
    def area(self):
        print("Area of Shape.")
        
class Circle(Shape):
    def area(self):
        print("Circle Area")
class Rectangle(Shape):
    def area(self):
        print("Rectangle Area")
        
obj = [Circle(), Rectangle()]
for i in obj:
    i.area() """