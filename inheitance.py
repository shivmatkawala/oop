# Inhritance :
    # Inheritance in oop concept where one class can reuse
    # properties and methods of other class.
    
    # A class which inherits properties / methods from other class
    # that class is called child class.
    
    # A class whose properies / methods are inherited by other class
    # is called parent class.
    

# calling parent method from object of child class.

# class A:  # parent class
#     def greet(self):
#         print("hello world")

# class B(A):  # child class
#     pass

# obj1 = B()
# obj1.greet()


# Overriding Method

# class A:  # parent class
#     def greet(self):
#         print("hello world")

# class B(A):  # child class
#     def greet(self):
#         print("Good bye dear..!")

# obj1 = B()
# obj1.greet()


#################################################

class A:
    def sound(self):
        return "This is A"
    
# class B(A):
#     pass

# obj_b = B()
# print(obj_b.sound())
