# Magic methods are the special methods that starts and ends with __ and 
# python calls it automatically under certain situation

# __init__
# __str__
# __len__
# __add__
# __sub__
# __mul__


class Student:
    
    def __init__(self, name, marks, roll):
        self.name = name
        self.roll = roll
        self.marks = marks
        
    def __str__(self):
        return f"{self.name} has scored {self.marks} marks."
    
    def __len__(self):
        return len("The __len__ magic method was called")
    
        
        
s1 = Student("Ujjwal",98,1)

print(Student)
print(s1)

s2 = Student("Ram",95,2)
print(s2)

# count = s1.len()
print(len(s1))


# class Number:
# def __init__(self, value):
# self.value = value
# def __add__(self, other):
# return self.value + other.value

# n1 = Number(10)
# n2 = Number(20)
# print(n1 + n2) # Automatically calls n1.__add__(n2)
