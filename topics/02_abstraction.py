# ABSTRACTION => It’s the action of determining the behavior of things in the real 
# life without thinking in their functioning, this with the goal of converting that 
# behavior into entities, objects or functions.

# Example:
# Problem => Create a basic calculator.

# First step:
# Think about what a basic calculator is? => It's a device that performs the most
# common mathematical operations in everyday life.

# Second step: 
# Determine that operations a basic calculator does  => Addition, subtraction, 
# multiplication and division.

# Third step:
# Establish how i will make the structure of the program or software => It will 
# have a Calculator class, within it i will create a method for each operation of 
# the calculator.

# Fourth step: 
# Create the structure of the program without going into detail about how it works.
class Calculator:
    def addition(): pass  #       <-╻
    #                               │
    def subtraction(): pass  #    <-│
    #                               │ => Abstraction
    def multiplication(): pass  # <-│
    #                               │
    def division(): pass  #       <-╹

# Fifth step:
# Create the functionality of each method, test it and use it.
class Calculator:
    def addition(self, num_1, num_2):  #       <-╻
        return num_1 + num_2 #                 <-│
    #                                            │
    def subtraction(self, num_1, num_2):  #    <-│
        return num_1 - num_2 #                 <-│
    #                                            │ => Implementation
    def multiplication(self, num_1, num_2):  # <-│
        return num_1 * num_2  #                <-│
    #                                            │
    def division(self, num_1, num_2):  #       <-│ 
        return num_1 / num_2  #                <-╹
    
basic_calculator = Calculator()

print(f"2 + 5 = {basic_calculator.addition(2, 5)}.")
print(f"2 - 5 = {basic_calculator.subtraction(2, 5)}.")
print(f"2 * 5 = {basic_calculator.multiplication(2, 5)}.")
print(f"2 / 5 = {basic_calculator.division(2, 5)}.")
