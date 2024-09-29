from vehicle import Vehicle

class CombustionVehicle(Vehicle):  # Child class of Vehicle, and parent class of 
    #                                Car.
    def __init__(self, brand, model, color, fuel_amount):
        # Import the constructor method from Vehicle.
        super().__init__(brand = brand, model = model, color = color)
        self.__fuel_amount = None
        
        self.fuel_amount = fuel_amount  # Use of the setter method or interface.

    @property 
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, liters):
        if liters > 70:
            print("!!!Overloaded tank: Liters should not be exceed of 70 liters.!!!")
        elif liters < 0:
            print("!!!Negative values are not allowed.!!!")
        else:
            self.__fuel_amount = liters
            
    def fuel_info(self):
        print("\nFuel information:\n")
        print(f"* Fuel amount: {self.fuel_amount} of 70 liters.\n")     
        