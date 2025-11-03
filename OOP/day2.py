# Inheritance
# Accessing the properties of parent class by child class

# class GrandParent:
# name = "GrandParent"
# def gf(self):
# print("This is from GrandParent class")

# class Parent(GrandParent):
# name = "Parent"
# def show(self):
# print("This is from Parent class")
        
# class Child(Parent):
# name = "Child"
# def abc(self):
# print("This is from Child class")
        
# child = Child()
# child.abc()
# child.show()
# child.gf()

# Multilevel Inheritance - Hierarchial Inheritance
# Child => Parent => Grandparent => GrandParentParent => GrandParentParentParent =>
# CHild can access the properties of grandpaent class directly


# Single Inheritance
# A child class inherits from a single parent class

# MultiInheritance
# A child class inherits from multiple parent classes

# class Animal:
# name = "Animal"
# def speak(self):
# print("Animal speaks")

# class Dog(Animal): # Dog inherits from Animal
# name = "Dog"
# def bark(self):
# print("Dog barks")
        
# def speak(self):
# print("Dog Speaks")

# d = Dog()
# d.speak() # from parent
# d.bark() # its own
# print(d.name)
# Methos overriding: Overwriting the methods of parent class in child class 

# a = Animal()
# print(a.name)
# a.speak()


class Student:
    name = "ABC"
    
class Parent:
    def show(self):
        print("This is from Parent class")
        
    def abc(self):
        print("ABC")
    

class Marks: 
    def show_marks (self):
            print("Marks got: 30")
    def abc(self):
        print("ABC from Marks")

class get_info(Student, Marks, Parent):
 pass
 
get = get_info()
get.show_marks()
print(get.name)
get.show()
get.abc()

print(get_info.mro())
        

# To solve the multiple inheritance diamond problem, python Has special technique called MRO
# Method Resolution Order
# Find the use of mro() method
