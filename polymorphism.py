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

class Apple:
        def __init__(self, color, origin, price):
                self.color  = color
                self._origin = origin
                self.__price =  price
                
        def get_info(self):
                print(f"Apple color is {self.color}.\nApple origin is {self._origin}.\nApple price is {self.__price}")
        
        
        
class Grape:
        def __init__(self, color, origin, price):
                self.color  = color
                self._origin = origin
                self.__price =  price
                
        def get_info(self):
                print(f"Grape color is {self.color}.\nGrape origin is {self._origin}.\nGrape price is {self.__price}")

oob1 = Apple("Red", "Kashmir", 200)
oob2 = Grape("Yellow", "Nashik", 100)

def get_fruit_info(obj):
        obj.get_info()
        
        
get_fruit_info(oob1)
print()
print()
get_fruit_info(oob2)