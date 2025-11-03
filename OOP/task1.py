# Task:
# Create a class student of a college "Mindrisers Institution"
# Add Class Attribute and Object Attribute

# Class keyword is used to define a class
# Syntax:
#     class class_name:
#         Attributes and methods

class Student:
    # Class Attribute (common for all students)
    college_name = "Mindrisers Institution"
    
    # Method to set Object Attributes (different for each student)
    def set_info(self, name, gender, address, marks):
        self.name = name
        self.gender = gender
        self.address = address
        self.marks = marks
        
    # Method to display student info
    def display(self):
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Address:", self.address)
        print("Marks:", self.marks)
        print("College:", self.college_name)
        

# Creating objects of Student class
Ram = Student()
Ram.set_info("Ram", "Male", "Putalisadak", 96)
Ram.display()

Sita = Student()
Sita.set_info("Sita", "Female", "Baneshwor", 97)
Sita.display()

Hari = Student()
Hari.set_info("Hari", "Male", "New Baneshwor", 95)
Hari.display()

# Accessing class attribute directly
print("All students study at:", Hari.college_name)
