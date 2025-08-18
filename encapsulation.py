# Encapsulation:-
    # Hiding unnecessary dunctionalities from user and
    # showcasing required one.
    
    # Types of Encapsulations:-
        # Public  :- Nothing is hidden {Inside the class 
        # and Outside of teh class}
        
        # Protected:- It can be accessed inside and outside of 
        # the class. but accessing outside of the class is not
        # recommended.
        
        # Private:- It can be accessed inside of the class but 
        # not outside of the class. but can be accessed with 
        # name mangling outside of the class too.
        
        

# class Square:
#     def __init__(self, side):
#         self.side = side   # public encapsulation
        
#     def area(self):
#         return f"Area of Square is {self.side ** 2}"
    
    
# class Rectangle:
#     def __init__(self, lenght, width):
#         self.length = lenght  # public  encapsulation
#         self._width = width  # protected encapsulation
        
#     def area(self):
#         return f"Area of a Rectangle is {self.length * self._width}"
        
        
# class Cuboid:
#     def __init__(self, length, width, height):
#         self.length = length   # public encapsulation
#         self._width = width     # protected encapsulation
#         self.__heigth = height   # Private Encapsulation
        
#     def volume(self):
#         return f"Volume of a Cuboid is {self.length * self._width * self.__heigth}"
    
    
    
# C1 = Cuboid(10, 5, 2)
# print(C1.volume())


# print(C1.length)
# print(C1._width)
# # print(C1.__heigth)    #'Cuboid' object has no attribute '__heigth'
# print(C1._Cuboid__heigth)  # name mangling



################################################


# class Square:
#     def __init__(self, side):
#         self.side = side
        
#     def area(self):    # public Encapuslation
#         ar = self.side ** 2
#         return ar
    
#     def is_big_square(self):
#         if self.area() > 50:
#             return "Big Square"
#         else:
#             return "Small Square"
        
# s1 = Square(5)
# print(s1.area())
# print(s1.is_big_square())



# class Cuboid:
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width = width
#         self.height = height
        
#     def area(self):   # public Encapsulation
#         return self.length * self.width
    
#     def _perimeter(self):  # protected Encapsulation
#         return (self.length * 2) + (self.width * 2)
    
#     def __volume(self):   # Private Encapsulation
#         return self.length * self.width * self.height
    
#     def is_big_cuboid(self):
#         if self.__volume > 50:
#             return "Big Volume"
#         else:
#             return "Small Volume"
        

# c1 = Cuboid(10, 5, 2)
# print(c1.area())  
# print(c1._perimeter())
# # print(c1.__volume())  #AttributeError: 'Cuboid' object has no attribute '__volume'

# print(c1._Cuboid__volume())   # name mangeling