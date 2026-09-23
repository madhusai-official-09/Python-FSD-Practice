# Create a Python program for a **Ride Booking System**.
# A customer can book different types of rides such as **Bike** or **Car**.
# ### Requirements:
# 1. Create an abstract class `Ride` with an abstract method `calculate_fare()`.
# 2. Create two child classes:
#         * `Bike`
#         * `Car`
# 3. Both classes should implement `calculate_fare()` differently.
# 4. Store the distance as a **private attribute** and provide methods to set and get the distance.
# 5. Create a `Customer` class to store the customer's name and pickup location.
# 6. Ask the user to select the ride type and enter the required details.
# 7. Display the customer details and calculated fare.
# ### Example Input:
# Enter customer name: Ravi
# Enter pickup location: Madhapur
# Enter distance: 10
# Enter ride type: Bike

# ### Expected Output:
# Customer: Ravi
# Pickup Location: Madhapur
# Ride Type: Bike
# Distance: 10 km
# Fare: 100
# Ride booked successfully
# **Assume:**
# * Bike fare = ₹10 per km
# * Car fare = ₹20 per km


# from abc import ABC, abstractmethod
# class Ride(ABC):
#     def __init__(self,d):
#         self.__distance = d 
        
#     def setdistance(self,d):
#         self.__distance=d
        
#     def getdistance(self):
#         return self.__distance
    
#     @abstractmethod
#     def calculate_fare(self):
#         pass

# class Bike(Ride):
#     def calculate_fare(self):
#         return self.getdistance()*10
        
# class Car(Ride):
#     def calculate_fare(self):
#         return self.getdistance()*20

from ride import Ride,Bike, Car
        
name = input("Enter Customer Name: ")
location = input("Enter pickup location: ")
d = int(input("Enter distance: "))
ride_type = input("Enter Ride type(Bike/Car): ")


def ride(d,ride_type):
    
    if ride_type.lower() == "bike":
        distance = d
        return Bike(distance)
    elif ride_type.lower() == "car":
        distance = d
        return Car(distance)
    else:
        print("Invalid ride type")
        return
fare = ride(d,ride_type)
res = fare.calculate_fare()
print("===== Ride Booking System =====")
print(f"Customer: {name}")
print(f"Pickup Location: {location}")
print(f"Ride Type: {ride_type}")
print(f"Distance: {d} km")
print(f"Fare: ₹{res}")
print("Ride booked successfully🎉")
