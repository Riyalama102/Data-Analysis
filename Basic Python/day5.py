# Procedural programming

dict1 = {
    "name":"Ujjwal",
    "surname":"Neupane",
    "age":29,
    "position":"Data Scientist"
}
values = dict1.values()
for i in values:
    print(i)
    
    
for i in dict1:
    print(dict1.get(i))

while True:
 num1 = int(input('Enter first number: '))
 num2 = int(input('Enter second number: '))
 operator = int(input('1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for power, 6 for closing: '))
 match operator:
  #case 1:
     #addition(num1,num2)
  case 2:
     print(num1 - num2)
  case 3:
   print(num1 * num2)
  case 4:
   print(num1 / num2)
  case 5:
   print(num1 ** num2)
  case 7:
   print("What in case 7")
  #case 8:
    # addition()
  case 6:
     break
  case _:
   print('Invalid operator')
            
# DRY - Don't Repeat Yourself
# Now we are heading towards the functional programming

# Code reusability => increase 
# Code optimizatin => increase

# def keyword is used to define a function
# Syntax:
# def function_name( parameters ):
# Code to be executed

# Only by defining the function, the function doesnot works
# We should call a function
# To call a function, we use function_name(Arguments)

a = 10
b = 5
def addition(): # Programmer/User defined function
 print(a+b)
 c=12
 print(c)
 return("Returning the statement")
sum = addition()


def subtraction(a,b,c):
 c=10
 print(a-b)
 print(c)


    
# # return keyword is used to return values
# # WHen return keyword returns something, we need a variable to store the returned value

# print("Print")
# input()
# type()
# int()
# float()

# Gobal Variable - The variable that is defined outside the function
# Local variable - The variable that is defined inside the function. 
# The local variable is only accessible inside the function where it is declared


# Arguents => The values we pass to a function during the function call
# Parameters => The variable that is used to store the arguments


def addition(num1,num2,num3): # Parameters are always local variables
 return num1+num2+num3

sum = addition(1,2,3)
print(sum)

# Arguments => There are 2 types of arguments
# Positional arguments (args) => single value arguments
# Keyword Arguments (kwargs) => Arguments those are in key-value pair

def display(name, age, degree):
 print("Name = ", name, "Age = ",age, "Degree = ", degree)
    
display(degree="Bachelors",age=29, name="Ujjwal")
    
# The most popular formatting string is f-string
def display(name, age, degree):
    # print("Name = ", name, "Age = ",age, "Degree = ", degree)
    print(f"Name = {name}, Age = {age}, Degrre = {degree}")
    
display(degree="Bachelors",age=29, name="Ujjwal")