# 1. Create a BankAccount class with a private variable balance. 
# Create methods: deposit(amount) withdraw(amount) displaybalance()

""" class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    
    def deposite(self,amount):
        if amount>0:
            self.__balance=self.__balance + amount
            
    def withdraw(self,w_amount):
        if self.__balance>w_amount:
            self.__balance = self.__balance - w_amount
    
    def display(self):
        return self.__balance
    
s1 = BankAccount(10000)
s1.deposite(2000)
s1.withdraw(5000)
ans = s1.display()
print(ans) """

# 2. Create an Employee class with a private variable salary. 
# Create: setsalary(salary) getsalary() The salary should be changed only through setsalary().

""" class Employee:
    def __init__(self,salary):
        self.__salary = salary
        
    def setsalary(self,update_salary):
        self.__salary = self.__salary+update_salary
    
    def getsalary(self):
        return self.__salary
    
emply1=Employee(30000)
emply1.setsalary(5000)
ans = emply1.getsalary()
print(ans) """

# 3. Create a User class with private variables username and password. 
# Create a method: login(username, password) The method should print Login Successful only when both username and password match.
            
""" class User:
    def __init__(self,name,password):
        self.__name = name
        self.__password = password
    def getter(self,name=input("Enter Your name: ").capitalize(),password=int(input("Enter password in integer: "))):
        if self.__name == name and self.__password == password:
            print("Login Successful")
        else:
            print("Try again...")

check = User("Madhu",123456)
check.getter() """

# 4. Create a Temperature class with a private variable temperature. 
# Create: settemperature(value) gettemperature()

""" class Temperature:
    def __init__(self,temperature):
        self.__temperature = temperature
    
    def settemperatre(self,value):
        self.__temperature = value
    def gettemperature(self):
        return f"Temperature is {self.__temperature}℃"

temp = Temperature(45)
ans = temp.gettemperature()
print(ans) """