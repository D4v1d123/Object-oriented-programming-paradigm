from shape import Shape

class Rectangle(Shape):  # Child class of interface or abstract class Shape.
    def __init__(self, dimensions, height, weight):
        self.__dimensions = int(dimensions)
        self.height = float(height)
        self.weight = float(weight)
    
    @property   
    def dimensions(self):  # Getter method.
        return self.__dimensions  #               <-╻
    #                                               │
    def get_area(self):  #                          │    Implementation or 
        return self.height * self.weight  #       <-│ => functionality of abstract
    #                                               │    methods.
    def get_perimeter(self):  #                     │    
        return 2 * (self.height + self.weight)  # <-╹