from vehicle import Vehicle

class ElectricVehicle(Vehicle):  # Child class of Vehicle, and parent class of Bike.
    def __init__(self, brand, model, color, charge_level, battery_condition):
        # Import the constructor method from Vehicle.
        super().__init__(brand = brand, model = model, color = color) 
        self.__charge_level = None
        self.__battery_condition = None
        
        self.charge_level = charge_level  #           <-╻ => Use of the setter 
        self.battery_condition = battery_condition  # <-╹    method or interface.
        
    @property
    def charge_level(self):
        return self.__charge_level
    
    @charge_level.setter
    def charge_level(self, value):
        if value > 100:
            print("!!!Overload: Load should not be exceed the 100%.!!!")
        elif value < 0:
            print("!!!Negative values are not allowed.!!!")
        else: 
            self.__charge_level = value   
        
    @property  
    def battery_condition(self):
        return self.__battery_condition  
    
    @battery_condition.setter
    def battery_condition(self, value):
        if value > 100:
            print("!!!The battery condition should not be exceed the 100%.!!!")
        elif value < 0:
            print("!!!Negative values are not allowed.!!!")
        else:
            self.__battery_condition = value  
            
    def curb(self):
        super().curb()  # Import the code block from method curb() of Vehicle.
        self.charge_level += 10  
    
    def battery_info(self):
        print("\nBattery information: \n")
        print(f"* Charge level: {self.charge_level}%. \n" + 
              f"* Battery condition: {self.battery_condition}%.\n")