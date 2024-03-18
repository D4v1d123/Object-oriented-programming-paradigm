from electric_car import ElectricCar
from gasoline_car import GasolineCar
from vehicle import Vehicle

# # Error: An abstract class cannot be directly instantiated.
# vehicle_01 = Vehicle("Ferrari", "FXX Evoluzione", "Gray-Black")

electric_car_01 = ElectricCar("Rimac", "Nevera", "Blue king")
gasoline_car_01 = GasolineCar("Apollo", "Intensa Emozione", "Yellow-Orange")

#                     ↓⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺╻
electric_car_01.reload_energy()  # │ => Same method (Poly), different behavior or 
gasoline_car_01.reload_energy()  # │    response depending on the class (morphism).
#                     ↑⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽╹