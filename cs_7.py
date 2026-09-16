# 1.What is a Class and what is an Object in Python? Explain the difference between a class and 
# an object with a suitable example. 
# Create a Car class with the attributes brand and model. Create a method to display the car details 
# and create objects for two different cars. 

""" class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def display(self):
        return f"Brand: {self.brand} \nModel: {self.model}"
    
c1 = Car("Toyota","Fortuner")
print(c1.display()) """

# 2.What are Access Modifiers in Python? Explain public, protected, and private members with 
# suitable examples. 
# Create a Library class where: 
# ->  book_name is a public member 
# ->  __book_id is a private member 
# ->  _available_copies is a protected member 
# Create an object and demonstrate how these members can be accessed.

""" class Library:
    def __init__(self,name,id,copies):
        self.book_name = name
        self.__book_id = id
        self._available_copies = copies
        
    @property
    def book_id(self):
        return self.__book_id
    
    def display(self):
        return f"Book Name: {self.book_name} \nBook_id: {self.book_id} \nAvailable_copies: {self._available_copies}"
    
l1 = Library("Python Programming", "B101", 5)
print(l1.display()) """

# 3.What is a Factory Method in Python? Explain how a factory method can be used to create 
# objects in different ways. 
# Create a Product class with name and price. Write a factory method that accepts a single string 
# such as "Laptop,55000" and creates a Product object by extracting the product name and price 
# from the string. 

""" class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def display(self):
        print(self.name)
        print(self.price)
        
class FactoryMethod:
    def createobject(self,input):
        product = ""
        price = 0
        for i in range(len(input)):
            if input[i]==",":
                product += input[0:i:1]
                price = input[i+1::1]
        return Product(product,price)
    
obj = FactoryMethod()
l1 = obj.createobject("Laptop,55000")
l1.display() """

# 4.What is Encapsulation in Python? Explain how encapsulation is used to protect the data of an 
# object. 
# Create a DigitalWallet class with a private __amount variable. Write methods to: 
#  Add money 
#  Spend money 
#  Display the available amount 
# The amount should not be directly accessible from outside the class. 

""" class DigitalWallet:
    def __init__(self, amount):
        self.__amount = amount
        
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self,value):
        added_amount = self.__amount + value
        self.__amount = added_amount
        
    def add_money(self,value):
        self.__amount += value
        print(f"Added {value} to wallet. New balance: {self.__amount}")
        
    def spend_money(self,value):
        if value <= self.__amount:
            self.__amount -= value
            print(f"Spent {value} from wallet. New balance: {self.__amount}")
        else:
            print("Insufficient funds.")

    def display_amount(self):
        print(f"Available amount in wallet: {self.__amount}")

a1 = DigitalWallet(1000)
a1.display_amount()
a1.add_money(500)
a1.spend_money(300)
a1.display_amount() """ 

# 5.What is Inheritance in Python? Explain how a child class can reuse the properties and 
# methods of a parent class. 
# Create a parent class Vehicle with brand and speed attributes and a method to display the 
# vehicle details. 
# Create a child class Bike that inherits from Vehicle and additionally has a helmet_required 
# attribute.Create a Bike object and display all the details using the child object. 
