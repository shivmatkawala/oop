# Polymorphism:-
        # In Programming , Polymorphism allows different 
        # classes or data types to use the same interface 
        # (method, operator or function) but behave differently.


# class Vehicle:
#         def start_vehicle(self):
#                 print("vehicle is started but dont know what vehicle")

#         def stop_vehicle(self):
#                 print("Vehicle is stopped")
                
                
# class Bugati(Vehicle):
#         # def start_vehicle(self):
#         #         print("Bugati is started")
        
#         def stop_vehicle(self):
#                 print("Bugati is stopped")
                
        

# class My_vehicle(Bugati):
#         def stop_vehicle(self):
#                 print("my vehichle is stopped")
          
# # b1 = Bugati()
# # b1.start_vehicle()
# # b1.stop_vehicle()

# m1 = My_vehicle()
# m1.start_vehicle()
# m1.stop_vehicle()


###########################


# class Animal:
#         def sound(self):
#                 print("-------")
                
                
# class Monkey(Animal):
#         # def sound(self):
#         #         print("woof")
#         pass
                
                
# m11 = Monkey()
# print(m11.sound())

############################################

# Types of Polymorphism: 

        # Duck type polymorphism
        # Method overridinng polymorphism
        # Operator Overloading
        # Function Polymorphism
        
        
        
# class Duck:
#         def speak(self):
#                 print("quack quack")
                
# class Dog:
#         def speak(self):
#                 print("woof ! woof !")
                

# obj1 = Duck()
# obj2 = Dog()

# def speak_it(obj):
#         obj.speak()
        
# speak_it(obj1)
# speak_it(obj2)


# wite a class called Apple, in that create a method which displays
# apple info

# wite a class called Grapes, in that create a method which displays
# grapes info

# class Apple:
#         def __init__(self, color, origin, price):
#                 self.color  = color
#                 self._origin = origin
#                 self.__price =  price
                
#         def get_info(self):
#                 print(f"Apple color is {self.color}.\nApple origin is {self._origin}.\nApple price is {self.__price}")
        
        
        
# class Grape:
#         def __init__(self, color, origin, price):
#                 self.color  = color
#                 self._origin = origin
#                 self.__price =  price
                
#         def get_info(self):
#                 print(f"Grape color is {self.color}.\nGrape origin is {self._origin}.\nGrape price is {self.__price}")

# oob1 = Apple("Red", "Kashmir", 200)
# oob2 = Grape("Yellow", "Nashik", 100)

# def get_fruit_info(obj):
#         obj.get_info()
        
        
# get_fruit_info(oob1)
# print()
# print()
# get_fruit_info(oob2)



#######################################

#1) Duck type:-

# class Ravi:
#         def personal_info(self):
#                 print("Hello my name is Ravi")

# class Vani:
#         def personal_info(self):
#                 print("Hello my name is Vani")
                
# class Sravanthi:
#         def personal_info(self):
#                 print("Hello my name is Sravanthi")
                

# obj1 = Ravi()
# obj2 = Vani()
# obj3 = Sravanthi()

# def get_personal_info(obj):
#         obj.personal_info()
        
# get_personal_info(obj1)
# get_personal_info(obj2)
# get_personal_info(obj3)


# Method Overloading:-
# Same method but different parameters.

# class Addition:
#         def addup(self, x=None, y=None, z=None):
#                 if x is not None and y is not None and z is not None:
#                         print(x + y + z)
                
#                 elif x is not None and y is not None and z is None:
#                         print(x + y)
                        
#                 elif x is not None and y is None and z is None:
#                         print(x)
                
#                 else:
#                         print(None)


# a1 = Addition()
# a1.addup(5, 10, 15)

# a2 = Addition()
# a2.addup(5, 10)

# a3 = Addition()
# a3.addup(5)

# a4 = Addition()
# a4.addup()


# class Demo:
#         def get_length(self,*args):
#                 print(args)
#                 if len(args) == 0:
#                         print("No element in list, it is empty")
#                 elif len(args) == 1:
#                         print("Only one element is present")
#                 elif len(args) == 2:
#                         print("Only 2 elements are present")
      
#                 else:
#                         print("Multiple elements are present")                
# d1 = Demo()
# d1.get_length()

# d2 = Demo()
# d2.get_length(1)

# d3 = Demo()
# d3.get_length(1, 2)

# d4 = Demo()
# d4.get_length(1, 2, 3)


# Method Overiding:
# Child class provides its own implementation
# of a method already defined in the parent class

# class Student:
#         def get_percentage(self):
#                 print("-- No Percenntage --")
                
                
# class Praveen(Student):
#         def get_percentage(self):
#                 print("My Last year percentage was 98 %")
                
# s1 = Student()
# s2 = Praveen()
# s1.get_percentage()
# s2.get_percentage()



# Operator Overloading:-

#   +       __add__(self, other)

#   -       __sub__(self, other)

#  *        __mul__(self, other)

#  /        __truediv__(self, other)

#  %        __mod__(self, other)

# ==        __eq__(self, other)

# <         __lt__(self, other)

# >         __gt__(self, other)

# len()     __len___(self, other)


# Engineering 1 st year there are 2 semesters:-
# percentage of year = sem1 percentage + sem2 percentage / 2

class Semester:
        def __init__(self, phy, chem, math):
                self.phy = phy
                self.chem = chem
                self.math = math
                
        def __add__(self, other):
                
        