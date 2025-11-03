# match is similar to the switch case in C.
# match keyword is used to define a matching condition and case keyword is used to check the matching value
a = 10
b = 20
choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division: "))
match choice:
    case 1 | 2 | 3:
        print(a+b)
    # case 2:
    # print(a-b)
    # case 3:
    # print(a*b)
    case 4:
        print(a/b)
    case _:
        print("Invalid Input")
        
# Day 2 
# Conditional statements works under the condition
# If the condition is true, then only the lines of code under conditional statements execute
# If the condition is false, the conditional statements is skiped

# IF - ELSE
# SYntax :
# if condition:
    # Lines of codes
# else:
    # Lines of code
    
a = 20
b = 10
if a < b:
 print("B is greater than A.")
else:
 print("A is greater than B.")


usernames = ["Ujjwal","ABC","DEF","GHI"]
username = input("Enter your username: ")
if username in usernames:
 print("Username found in usernames.")
else:
 print("Username not found.")
    

user_dict = {
             "Ujjwal":"Ujjwal123",
             "Ram":"Ram123",
             "Shyam":"Shya123"
            }
usernames = user_dict.keys()
passwords = user_dict.values()
print(usernames)
print(passwords)

username = input("ENter your username: ")
if username in user_dict:
 print("Username found")
else:
 print("Username not found")
    

# LOOPS
# LOOPS are used when we need to repeat a same block of code multiple times
# There are 2 types of loops in Pyhton => FOR and WHILE
# For loop is used when we already know the start and stop condition
# While loop is used when we dont know the start and stop condition

# Syntax: 
# For 

# for iterator in iterable(group data type):
    # Code to be executed
    
# Iteraor is simply a variable that is used to count the iteration 

# Iteration is a single round that is executed when a loop is encountered

user_dict = {
"Ujjwal":"Ujjwal123",
"Ram":"Ram123",
"Shyam":"Shya123"
}
print(usernames)
for i in usernames:
 print(i)
 #Upto here Day 2


# Day 3
# for keyword is used in for loop => For loop is used when we already know the start and end value
# while keyword is used in while loop => While loop is used when we dont know the stopping condition 

list = ["Ujjwal","Neupane",5,8,9,6]
for i in list:
 print(i)
    
tuple = ("Ujjwal","Neupane",5,8,9,6)
for i in tuple:
 print(i)
    
user_dict = {
"Ujjwal":"Ujjwal123",
"Ram":"Ram123",
"Shyam":"Shya123"
}
usernames = user_dict.keys()
print(usernames)
values = user_dict.values()
print(values)
for i in values:
 print(i)

for i in user_dict:
 print(user_dict.get(i))

# range() => Generates the value. Range takes 3 values => start, end, step

for i in range(5,12,2):
 print(i)

for i in range(0,101,3):
 print(i)



list = ["Ujjwal" for x in range(1,101)]
print(list)
# USe of list comprehension
# We use loop inside the list
