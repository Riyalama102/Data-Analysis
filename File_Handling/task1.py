#Prepare a simple login and register system using File and function only of usernames.
# Function to register username
def register():
    username = input("Enter your username: ")
    file = open("test1.txt", "a")
    file.write(username + "-")
    file.close()
    print("Registration Successful")

# Function to login
def login():
    file = open("test1.txt", "r")
    content = file.read()
    file.close()

    usernames = content.split("-")
    usernamel = input("Enter your username: ")

    if usernamel in usernames:
        print("Login Successful")
    else:
        print("Login Failed")

# Main program
print("1. Register")
print("2. Login")
choice = input("Enter your choice (1/2): ")

if choice == "1":
    register()
elif choice == "2":
    login()
else:
    print("Invalid choice")

#Python Exercise
# Task 1: Make a calculator program using Python functions and loop

def calculator():
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting calculator...")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)
        elif choice == "2":
            print("Result:", num1 - num2)
        elif choice == "3":
            print("Result:", num1 * num2)
        elif choice == "4":
            print("Result:", num1 / num2)
        else:
            print("Invalid choice!")

calculator()


# Task 2: Print a multiplication table of the number that is input by the user

def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

multiplication_table()


# Task 3: Check if the given number is even or odd

def even_or_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

even_or_odd()


# Task 4: Check if a given number is palindrome or not

def check_palindrome():
    num = input("Enter a number: ")
    if num == num[::-1]:
        print("The number is Palindrome")
    else:
        print("The number is Not Palindrome")

check_palindrome()


# Task 5: Make a simple login system without registration using functions

def login_system():
    username = "admin"
    password = "1234"

    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == username and pwd == password:
        print("Login Successful")
    else:
        print("Login Failed")

login_system()


# Task 6: Make a login system using registration using function

def register():
    username = input("Enter your username: ")
    file = open("users.txt", "a")
    file.write(username + "-")
    file.close()
    print("Registration Successful")

def login():
    file = open("users.txt", "r")
    content = file.read()
    file.close()

    usernames = content.split("-")
    usernamel = input("Enter your username: ")

    if usernamel in usernames:
        print("Login Successful")
    else:
        print("Login Failed")

print("1. Register")
print("2. Login")
choice = input("Enter your choice (1/2): ")

if choice == "1":
    register()
elif choice == "2":
    login()
else:
    print("Invalid choice")


# Task 7: Print all the even numbers in a list of numbers

def print_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Even numbers are:")
    for num in numbers:
        if num % 2 == 0:
            print(num)

print_even_numbers()


