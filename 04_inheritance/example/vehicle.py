class Vehicle:  # Parent class or super class of ElectricVehicle and 
    #             CombustionVehicle.
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        
    def speed_up(self):
        print("The vehicle is accelerating.")
        
    def curb(self):
        print("The vehicle is braking.")