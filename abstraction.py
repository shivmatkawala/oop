# Abstraction:-
    # Abstraction is an OOP concept that hides implementation
    # details and exposes only the necessary features to the user.
    
    
# How to achieve abstraction in Python:-
    # Python provides abstraction mainly through Abstract Base
    # Classes (ABC) using abc module.
    
    
    #  Ex:-
    
from abc import ABC, abstractmethod
from math import pi
# Creating a abstract class:

class M(ABC):           # Abstract class
    
    @abstractmethod     # method is abstarctmethod
    def alpha(self):
        pass
    

# class N(M):
#     def greet(self):
#         print("Hello World")
        

# obj_n = N()   #  TypeError: Can't instantiate abstract class N without an implementation for abstract method 'alpha'


# class O(M):
#     name = "Ravi"
    
#     def alpha(self):
#         print("This is alpha")
    
#     def greet(self):
#         print("Hello World")
    
#     @classmethod 
#     def myName(cls):
#         print(f"Your name is {cls.name}")
        

# obj_o = O()
# obj_o.alpha()
# obj_o.greet()
# obj_o.myName()



# create a class called shape which will inherite ABC.
# create a concrete class circle, rectangle, rat, these classes
# will inherite class shape.

# shape:- 2-d shapes [different properties, but same methods]

# class Shape(ABC):
    
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass
    

# class Circle(Shape):
    
#     def __init__(self, radius):
#         self.radius = radius
#         super().__init__()
        
#     def area(self):
#         return f"Area of Circle is {pi * (self.radius ** 2)}"
    
#     def perimeter(self):
#         return f"Perimeter of Circle is {2 * pi * self. radius}"
    

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
        
#         super().__init__()
    
#     def area(self):
#         return f"Area of Rectangle is {self.length * self.width}"
    
#     def perimeter(self):
#         return f"Perimeter of Rectangle is {(self.length * 2) + (self.width * 2)}"
    
    
# class Rat(Shape):
#     def __init__(self, base, height, hypoteneous):
#         self.base = base
#         self.height = height
#         self.hypoteneous = hypoteneous
        
#         super().__init__()
        
#     def area(self):
#         return f"Area of Right Angle Triangle is  {0.5 * self.base * self.height}"
    
#     def perimeter(self):
#         return f"Perimeter of Right angle Triangle is {self.height + self.base + self.hypoteneous}"
    
    
# obj_circle = Circle(5)
# print(obj_circle.area())
# print(obj_circle.perimeter())

# obj_rectangle = Rectangle(10, 5)

# print(obj_rectangle.area())

# print(obj_rectangle.perimeter())


# obj_rat = Rat(3, 4, 5)
# print(obj_rat.area())
# print(obj_rat.perimeter())


# create an abstract class called Vehicle.
# create start, stop, horn abstract methods.

# create concrete classes like  Car, Bus, Truck
# inherite in each concrete class class Vehicle.
# Implement all Abstract class methods.
# in each class also crete one static method and one classmethod.