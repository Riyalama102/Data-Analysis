# To solve the multiple inheritance diamond problem,
# Python has a special technique called MRO (Method Resolution Order)

# MRO defines the order in which methods are searched
# when a class is involved in multiple inheritance.

class Student:
    name = "ABC"
    
class Parent:
    def show(self):
        print("This is from Parent class")
        
    def abc(self):
        print("ABC from Parent class")
    

class Marks: 
    def show_marks(self):
        print("Marks got: 30")
    def abc(self):
        print("ABC from Marks class")

# Multiple inheritance
# get_info class inherits from Student, Marks, and Parent
class get_info(Student, Marks, Parent):
    pass

get = get_info()
get.show_marks()
print(get.name)
get.show()
get.abc()   # which abc() runs depends on MRO

# Showing the Method Resolution Order
print("\nMethod Resolution Order (MRO):")
print(get_info.mro())
