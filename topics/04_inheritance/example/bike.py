from electric_vehicle import ElectricVehicle

class Bike(ElectricVehicle):  # Child class of ElectricVehicle.
    def wheelie(self):
        print("The bike is doing a wheelie.")      


bike_01 = Bike("Specialized", "Tarmac SL7", "Gray-Black", 68, 80)
bike_01.charge_level = 120
bike_01.charge_level = 60
bike_01.battery_condition = 70
bike_01.battery_info()
bike_01.wheelie()
bike_01.curb()
bike_01.battery_info()