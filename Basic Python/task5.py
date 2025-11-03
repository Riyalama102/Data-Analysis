# Task: Calculator
# Update this task using functions and loop


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculator():
    while True:
        print("\n--- Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", add(a, b))

            case 2:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", subtract(a, b))

            case 3:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", multiply(a, b))

            case 4:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", divide(a, b))

            case 5:
                print("Exiting Calculator...")
                break

            case _:
                print("Invalid choice! Try again.")

# Run the calculator
calculator()

# Task: Accounting
# Update this task using functions and loop

accounts = {"user1": 1000, "user2": 500}  # dictionary for username & balance

def check_balance(username):
    print(f"Your balance is: {accounts[username]}")

def add_balance(username):
    amount = float(input("Enter amount to add: "))
    accounts[username] += amount
    print("Balance updated! New balance:", accounts[username])

def withdraw_balance(username):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= accounts[username]:
        accounts[username] -= amount
        print("Withdrawal successful! New balance:", accounts[username])
    else:
        print("Insufficient balance!")

def accounting():
    while True:
        username = input("\nEnter username (or type 'exit' to quit): ")
        if username == "exit":
            print("Exiting Accounting System...")
            break

        if username in accounts:
            print(f"Welcome {username}!")
            while True:
                print("\n1. Check Balance")
                print("2. Add Balance")
                print("3. Withdraw Balance")
                print("4. Logout")
                choice = int(input("Enter your choice: "))

                match choice:
                    case 1:
                        check_balance(username)
                    case 2:
                        add_balance(username)
                    case 3:
                        withdraw_balance(username)
                    case 4:
                        print("Logging out...")
                        break
                    case _:
                        print("Invalid choice!")
        else:
            print("User not found!")

# Run the accounting system
accounting()

