# Task: Update every program we have done using try except

# Calculator using try-except

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operator!")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
    print("Unexpected error:", e)


# Check if number is even or odd using try-except

try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is Even.")
    else:
        print(num, "is Odd.")
except ValueError:
    print("Error: Please enter a valid integer.")


# Check if number is palindrome using try-except

try:
    num = int(input("Enter a number: "))
    if str(num) == str(num)[::-1]:
        print(num, "is a palindrome.")
    else:
        print(num, "is not a palindrome.")
except ValueError:
    print("Error: Please enter a valid number.")


# Login and registration system using try-except

try:
    users = {}

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            users[username] = password
            print("Registration successful!")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username in users and users[username] == password:
                print("Login successful!")
            else:
                print("Invalid username or password!")

        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")

except Exception as e:
    print("Error occurred:", e)
