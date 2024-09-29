from abc import ABC, abstractmethod  # The abc library allows you create and manage 
# abstract classes.

# Create an abstract class or interface.
#            ↓
class Shape(ABC):
    @property  #       <-╻ => Define a getter method to force the classes to 
    @abstractmethod  # <-╹    implement the "dimensions" attribute.
    def dimensions(self):  #    <-╻
        pass  #                   │
    #                             │
    @abstractmethod  #            │ 
    def get_area(self):  #      <-│ => Abstract methods that the classes must 
        pass #                    │    implement and define their functionality. 
    #                             │
    @abstractmethod  #            │
    def get_perimeter(self):  # <-╹
        pass