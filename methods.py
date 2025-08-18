

# Write a class for Rectangle.

    # properties :-  length, width, color
    # methods:- area, perimeter, is_big_or_small, greet
    
# class Rectangle:
#     count = 0
#     def __init__(self, length, width, color):
#         self.length = length
#         self.width = width
#         self.color = color
#         Rectangle.get_count_of_obj()
#     def area(self):   #instance method
#         return f"Area of a rectnagle is {self.length * self.width}"
    
#     @staticmethod
#     def greet(name):
#         return f"Hello {name}"
    
    
#     @classmethod
#     def get_count_of_obj(cls):
#         cls.count+=1
    
#     def perimeter(self):   # instance method
#         return f"Perimeter of a rectangle is {(self. length + self.width)*2}"
    
#     def __str__(self):
#         return "Hello from Rectangle"
    
# obj1 = Rectangle(5, 2, 'black')
# obj2 = Rectangle(10, 4, "Blue")
# obj3 = Rectangle(15, 6, "Green")
# obj4 = Rectangle(3, 1, 'yellow')
# print(obj1.area())
# print(obj2.area())
# print(obj3.area())

# print(obj1.greet("vani"))
# print(Rectangle.greet("Soni"))
# print(Rectangle.count)
# print(Rectangle(6, 3, "pink"))



##########################################################



# Create a class called Car: [Instance Method]

# class Car:
#     wheels = 4   #  class variable
    
#     # constructor
#     def __init__(self, brand, color, gears):
#         self.brand = brand    # instance variable
#         self._color = color   # private instance variable
#         self.__gears = gears  # protected instance variable
        
#     # Instance Method
#     def start(self):
#         print(f"{self.brand} car is starting..!")
        
        
#     # Class Method
#     @classmethod       # <-- decorator
#     def get_wheel_count(cls):
#         print(f"A car has {cls.wheels} wheels.")
        
    
#     # Static Method
#     @staticmethod      # <-- decorator
#     def fuel_type():
#         print("Petrol or Diesel")
        
        
#     # Special/ Magic/ Dunder Method
#     def __str__(self):
#         return "This class is about Car"
        
#     # Property Method
#     @property        # <-- decorator
#     def get_brand(self):
#         print(f"{self.brand}") 
        
        
#     @property
#     def get_gears(self):
#         print(f"{self.__gears}")
    
        
# car1 = Car("Mercedez Benz", "Yellow", 4)
# car2 = Car("Audi", "Pink", 6)

# car1.start()    # Instance methods will be accessed by calling object first
# car2.start()    # Instance methods will be accessed by calling object first

# car1.get_wheel_count()
# car2.get_wheel_count()


# car1.fuel_type()
# car2.fuel_type()

# print(car1)
# print(car2)

# car1.get_brand
# car2.get_brand

# print(car1._color)
# print(car2._color)


# # print(car1.__gears)
# # print(car2.__gears)
# print(car1.get_gears)
# print(car2.get_gears)



#######################################################


# write a class called Bank: 
# [instance, class, static, special, property methods]


class Bank:
    city = "Hyderabad"
    
    def __init__(self, name, branch, ifsc, manager, contact):
        self.name = name 
        self.branch = branch
        self.ifsc = ifsc
        self.manager = manager
        self.contact = contact
        
    # instance method
    def get_bank_details(self):
        return f"Bank Name: '{self.name}'\nIFSC Code: '{self.ifsc}'\nCity: '{self.city}'\nPhone: '{self.contact}'"
    

obj1 = Bank('Canara Bank', 'Musapet', 'HYDM100045', 'Shiva Akula', '+91-445-667')

print(obj1.get_bank_details())