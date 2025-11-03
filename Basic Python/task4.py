# 1. Task: Ask username from user, append the username in list,
# ask username from user, check if username present in list,
# if yes => print("Login successful") else print("Login failed")

users = []  # empty list

# Register username
username = input("Enter a username to register: ")
users.append(username)

# Login
login_name = input("Enter username to login: ")
if login_name in users:
    print("Login successful")
else:
    print("Login failed")


# 2. Task: Updated version of previous task. 
# 1 for register, 2 for login.
# 1 ask username and append in list.
# 2 ask username and check if username is present or not.

users = []

choice = int(input("Enter 1 to Register or 2 to Login: "))

if choice == 1:
    username = input("Enter username to register: ")
    users.append(username)
    print("User registered successfully!")

elif choice == 2:
    username = input("Enter username to login: ")
    if username in users:
        print("Login successful")
    else:
        print("Login failed")

else:
    print("Invalid choice!")


# 3. Task: Update this program using loop

users = []

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter username to register: ")
        users.append(username)
        print("User registered successfully!")

    elif choice == 2:
        username = input("Enter username to login: ")
        if username in users:
            print("Login successful")
        else:
            print("Login failed")

    elif choice == 3:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")


# 4. Task: Update Calculator using loop.

while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting Calculator...")
        break
    else:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", a + b)
        elif choice == 2:
            print("Result:", a - b)
        elif choice == 3:
            print("Result:", a * b)
        elif choice == 4:
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Division by zero")
        else:
            print("Invalid choice! Try again.")


# 5. Task: Use nested loop and nested if else to create a program and explore it.

for i in range(1, 4):  # outer loop
    print(f"\nOuter Loop Iteration {i}")
    
    for j in range(1, 4):  # inner loop
        print(f"  Inner Loop Iteration {j}")

        if j % 2 == 0:
            if i % 2 == 0:
                print("   Both i and j are even")
            else:
                print("   j is even but i is odd")
        else:
            if i % 2 != 0:
                print("   Both i and j are odd")
            else:
                print("   j is odd but i is even")


# 6. Task: Make an accounting system where a user logins
# and he should be able to check the balance,
# add balance and withdraw balance.
# Use dictionary, IF...ELSE and loop if needed.

accounts = {"user1": 1000, "user2": 500}  # dictionary with usernames & balances

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

            if choice == 1:
                print("Your balance is:", accounts[username])

            elif choice == 2:
                amount = float(input("Enter amount to add: "))
                accounts[username] += amount
                print("Balance updated! New balance:", accounts[username])

            elif choice == 3:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= accounts[username]:
                    accounts[username] -= amount
                    print("Withdrawal successful! New balance:", accounts[username])
                else:
                    print("Insufficient balance!")

            elif choice == 4:
                print("Logging out...")
                break
            else:
                print("Invalid choice!")
    else:
        print("User not found!")


