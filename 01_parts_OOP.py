
# OBJECT-ORIENTED PROGRAMMING => It's a paradigm that extracts the features and 
# functionality from the real world through class, objects, attributes and methods.

# OBJECT => It’s an abstraction or conceptualization of an element from the real 
# world, it has attributes and methods.

# CLASS => It’s a template to create objects. The class name has the first word  
# capitalized. 

# ATTRIBUTES => They are the features of an object, for example, color, location, 
# name, sex, etc.

# METHOD => They are the actions or functionalities of an object, for example, 
# shopping, sleeping, speaking, walking etc.

# CONSTRUCTOR METHOD => It initializes the attributes of an object. It is named 
# as __init__.

# INSTANTIATE => Create an object.
class Person:  # Class
    def __init__ (self, name, phone_number, email, location):  # Constructor method
        self.name = name
        self.phone_number = phone_number  # Attribute.
        self.email = email
        self.location = location
    
    def greeting(name):  # Method
        print(f"Hello {name}.")


# Object  Class            Attribute
#   ↓       ↓                  ↓
User_1 = Person("mariana", 3142915739, "marian14@gmail.com", "tunja")
#      ↑       ↑                                                    ↑
#      │       ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
# Instantiate                    Constructor method