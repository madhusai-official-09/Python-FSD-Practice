from abc import ABC, abstractmethod
class Ride(ABC):
    def __init__(self,d):
        self.__distance = d 
        
    def setdistance(self,d):
        self.__distance=d
        
    def getdistance(self):
        return self.__distance
    
    @abstractmethod
    def calculate_fare(self):
        pass

class Bike(Ride):
    def calculate_fare(self):
        return self.getdistance()*10
        
class Car(Ride):
    def calculate_fare(self):
        return self.getdistance()*20
    
class Customer:
    def __init__(self,name,location):
        self.name = name
        self.location = location