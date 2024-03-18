from abc import ABC, abstractmethod  # Library to creating abstract classes and 
#                                      methods.  

# Set a class as abstract class.
#              ↓
class Vehicle(ABC):  # Parent class of ElectricCar and GasolineCar.
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    @abstractmethod  # Set a method as abstract method.
    def reload_energy(self):
        pass