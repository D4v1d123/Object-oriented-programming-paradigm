from combustion_vehicle import CombustionVehicle

class Car(CombustionVehicle):  # Child class of CombustionVehicle.
    def burnout(self):
        print("The car is burning tires.")
        

car_01 = Car("Porche", "Carrera GT", "Gray", 48)
car_01.fuel_info()
car_01.fuel_amount = 80
car_01.fuel_amount = 20
car_01.fuel_info()
car_01.speed_up()
car_01.curb()

