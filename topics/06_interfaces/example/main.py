from circle import Circle
from rectangle import Rectangle

# Enter data.
print("Enter circle data in meters:")
dimensions = input("* Number of dimensions: ")
radius = input("* Radius: ")

print("\nEnter rectangle data in meters:")
dimensions = input("* Number of dimensions: ")
height = input("* Height: ")
weight = input("* Weight: ")

# Create objects.
circle = Circle(dimensions, radius)
rectangle = Rectangle(dimensions, height, weight)

# Show results.
print(f"\n\nCIRCLE: \n* {circle.dimensions}D figure. \n* The area is {circle.get_area()} m."  
    f"\n* The perimeter is {circle.get_perimeter()} m.\n")

print(f"RECTANGLE: \n* {circle.dimensions}D figure. \n* The area is {rectangle.get_area()} m." 
    f"\n* The perimeter is {rectangle.get_perimeter()} m.")