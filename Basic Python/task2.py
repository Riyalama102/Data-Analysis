#Day 2: Task
#Task 1: List of usernames
# Create a list of usernames
usernames = ["Riya", "Ram", "Shyam", "Hari"]

# Input from user
username = input("Enter your username: ")

# Check if the username exists
if username in usernames:
    print("Username found in the list.")
else:
    print("Username not found in the list.")

#Task 2: Dictionary of usernames & passwords
# Create dictionary
user_dict = {
    "Riya": "Riya123",
    "Ram": "Ram123",
    "Shyam": "Shyam123",
    "Hari": "Hari123"
}

# Extract usernames (keys from dictionary)
usernames = list(user_dict.keys())   # ['Riya', 'Ram', 'Shyam', 'Hari']
print("All usernames:", usernames)

# Input from user
username = input("Enter your username: ")

# Check if username exists in extracted list
if username in usernames:
    print("Username found in dictionary keys.")
else:
    print("Username not found in dictionary keys.")

#Task 3: Calculator Program (Using If-Else)
# Simple calculator using IF ELSE

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operator")

#Task 4: Login Program (Dictionary + If else)
# Dictionary with usernames and passwords
user_dict = {
    "Riya": "Riya123",
    "Ram": "Ram123",
    "Shyam": "Shyam123"
}

# Input username & password
username = input("Enter username: ")
password = input("Enter password: ")

# Check username and password
if username in user_dict:
    if user_dict[username] == password:
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Username not found")

#Task 5: Greatest & Smallest Among Three Numbers (Using If-ELse + Logical Operators)
# Find greatest and smallest among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Greatest number
if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

# Smallest number
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print("Greatest number:", greatest)
print("Smallest number:", smallest)



