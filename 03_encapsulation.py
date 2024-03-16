# --------------------------------------------------------------------------------
# Encapsulation => Allows you hide implementation details of an object (attribute 
# and method), preventing them from being accessible of insecure or erroneous way.
# Public and private visibility limit access to attributes and methods in 
# programming, but in python everything is public, because of this, the behavior 
# of private visibility must be simulated.

# Public visibility => Attributes and methods can be accessed from anywhere in the
# software or program.

# Private visibility: Attributes and methods can only be accessed within the class
# where they were declared.

# @property interface (getter) => It’s a decorator function that allow you access
# and obtain the value of a private attribute of a secure way.

# @getter_method_name.setter interface (setter) => It’s a decorator function that
# allows you to modify a private attribute of secure way, avoiding syntax and logic
# errors. 
class Car:
    fuel_type = "gasoline"  #                                         <-╻ 
    #                                                                   │
    def __init__(self, brand, model, fuel_tank_level, engine_status):  #│ => Public
        self.brand = brand  #                                         <-│ variable.
        self.model = model  #                                         <-╹ 
        self._fuel_tank_level = fuel_tank_level  # Private variable (implementation 
        #                                          attributes "_attribute").
        self.__engine_status = engine_status  # Public variable (special attributes 
        #                                       "__attribute").

    @property  # Getter method.
    def fuel_tank_level(self):
        return self._fuel_tank_level
    
    @fuel_tank_level.setter  # Setter method.
    def fuel_tank_level(self, fuel_info):
        liters, type_fuel = fuel_info
        
        if (liters + self._fuel_tank_level <= 70) and type_fuel == "gasoline":
            self._fuel_tank_level += liters  # Assign the value to the private 
        #                                      attribute. 
        elif type_fuel != "gasoline":
            print("!!!Wrong fuel type.!!!")
        else: 
            print("!!!Exceeds fuel tank capacity.!!!")
        
    @property  # Getter method.
    def engine_status(self):
        return self.__engine_status

    @engine_status.setter  # Setter method.
    def engine_status(self, oil_level):
        if (oil_level >= 0) and (oil_level <= 100):
            self.__engine_status += (oil_level * 15) / 100  # Assign the value to 
        #                                                     the private attribute. 
        else:
            print("!!!Wrong oil level.!!!")
            
            
car = Car("Porche", "GT3 RS", 10, 50)

print("Specifications:")
print(f"* Brand: {car.brand}. \n* Model: {car.model}.")
print(f"* Fuel tank level: {car.fuel_tank_level}%. \n* Engine status: {car.engine_status}%.")

car.fuel_tank_level = (53, "diesel")
car.fuel_tank_level = (53, "gasoline")
car.engine_status = 90

print("\nSpecifications:")
print(f"* Brand: {car.brand}. \n* Model: {car.model}.")
print(f"* Fuel tank level: {car.fuel_tank_level}%. \n* Engine status: {car.engine_status}%.")

