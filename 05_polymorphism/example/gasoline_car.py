from vehicle import Vehicle

class GasolineCar(Vehicle):  # Child class of Vehicle.
    def reload_energy(self):
        print("Refilling the tank at a fuel station.")
        