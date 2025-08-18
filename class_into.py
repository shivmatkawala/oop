# class Square:
#   def __init__(self, side,  color):
#     self.side = side
#     self.color = color
    
#   def area(self):
#     return f"Area of Square is {self.side * self.side}"
    
#   def perimeter(self):
#     return f"Perimeter of Square is {4 * self.side}"


# square :- side -> 5, color -> green

# sq1 = Square(5, "green")

# print(sq1.area())
# print(sq1.perimeter())
# print(sq1.color)
# print(sq1.side)

# print("---------------------------")

# square :- side -> 8, color -> yellow

# sq2 = Square(8, "Black")
# print(sq2.area())
# print(sq2.perimeter())
# print(sq2.color)
# print(sq2.side)

##############################################

# write a class representing employee.

# class Employee:
#   # constructor :- it is also a method but it is a dunder/ special method.
#   # constructor takes class arguments [properties] and inititalize them.
#   def __init__(self, empFirstName, empLastName, empId, empEmail, empContact, empPosition, empQualification, empCompanyName, empSalary):
#     self.empFirstName = empFirstName
#     self.empLastName = empLastName
#     self.empId = empId
#     self.empEmail = empEmail
#     self.empContact = empContact
#     self.empPosition = empPosition
#     self.empQualificatio = empQualification
#     self.empCompanyName = empCompanyName
#     self.empSalary = empSalary
    
#   def emp_full_name(self):
#     return f"{self.empFirstName} {self.empLastName}"
  
#   def emp_inhand_salary(self):
#     inhand = self.empSalary - (20/100) * self.empSalary
#     return f"In hand salary of {self.empFirstName} is {inhand}"
  
#   def emp_contact_details(self):
#     return f"Email Id of {self.empFirstName} is {self.empEmail}\nMobile number is {self.empContact}"



# emp1 = Employee("Manasa", "Reddy", "tcs101", 'manasareddy@tcs.com', 9988776655, 'Sr. Developer', 'B.Tech', "TCS",120000)

# print(emp1.emp_full_name())

# print(emp1.emp_inhand_salary())

# print(emp1.emp_contact_details())



# emp2 = Employee('Pravin', 'Voilet', 'cog1002', 'pravinv@cognizant.com', 6677889900, 'Sr. Data Scientist', "B. Tech", "Cognizant", 180000)

# print(emp2.emp_full_name())


# create a class of bank holder.



# write a class for circle.
import math

class Circle:
  pi = 3.14       # class variable
  def __init__(self, radius):
    self.r = radius       # Instance Variable
    
  def area(self):
    return f"Area of Circle is {self.pi* (self.r ** 2)}"
  
  def perimeter(self):
    return f"Perimeter of Circle is {2 * self.pi * self.r}"
  
  def get_diamesions(self):
    shape = "2-D"         # local variable
    return f"Circle is {shape} diamensional."


c1 = Circle(12)
print(c1.area())
print(c1.perimeter())
print(c1.pi)        # access pi value by calling a object of class
print(Circle.pi)    # access pi value by calling a classname