from shape import Shape

class Circle(Shape):  # Child class of interface or abstract class Shape.
    def __init__(self, dimensions, radius):
        self.__dimensions = int(dimensions)
        self.radius = float(radius)
        self.pi_number = 3.141592
    
    @property
    def dimensions(self):  # Getter method.
        return self.__dimensions  #                   <-╻
    #                                                   │
    def get_area(self):  #                              │    Implementation or 
        return self.pi_number * (self.radius ** 2)  # <-│ => functionality of 
    #                                                   │    abstract methods.
    def get_perimeter(self):  #                         │    
        return 2 * self.pi_number * self.radius  #    <-╹