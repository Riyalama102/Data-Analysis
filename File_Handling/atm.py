# Task:
# Prepare an ATM system that includes register and login system
# and the user is able to add balance, check balance, withdraw balance.
# Use files.

import json
import os

# Register new user
def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    # Save credentials to file
    credentials = {username: password}
    json_data = json.dumps(credentials)

    with open("login.txt", "a") as f:
        f.write(json_data + "-")

    # Initialize balance = 0 for new user
    with open("atm.txt", "a") as f:
        f.write(json.dumps({username: 0}) + "-")

    print("Registration Successful!\n")


# Login existing user
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not os.path.exists("login.txt"):
        print("No users registered yet.")
        return None

    with open("login.txt", "r") as f:
        content = f.read()

    users = content.split("-")
    for u in users:
        if u.strip() != "":
            data = json.loads(u)
            if username in data and data[username] == password:
                print(f"Login Successful! Welcome, {username}\n")
                return username
    else:
        print("Invalid username or password.\n")
        return None

# Get balance of user
def get_balance(username):
    with open("atm.txt", "r") as f:
        content = f.read()

    records = content.split("-")
    for r in records:
        if r.strip() != "":
            data = json.loads(r)
            if username in data:
                return data[username]
    return 0

# Update balance in file
def update_balance(username, new_balance):
    with open("atm.txt", "r") as f:
        content = f.read()

    records = content.split("-")
    updated_records = []
    found = False

    for r in records:
        if r.strip() != "":
            data = json.loads(r)
            if username in data:
                data[username] = new_balance
                found = True
            updated_records.append(json.dumps(data))

    if not found:
        updated_records.append(json.dumps({username: new_balance}))

    with open("atm.txt", "w") as f:
        f.write("-".join(updated_records) + "-")

# ATM Menu after login
def atm_menu(username):
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Add Balance")
        print("3. Withdraw Balance")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            balance = get_balance(username)
            print(f"Your current balance is: Rs. {balance}")

        elif choice == "2":
            amount = float(input("Enter amount to add: "))
            balance = get_balance(username)
            new_balance = balance + amount
            update_balance(username, new_balance)
            print(f"Rs. {amount} added successfully!")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            balance = get_balance(username)
            if amount > balance:
                print("Insufficient balance!")
            else:
                new_balance = balance - amount
                update_balance(username, new_balance)
                print(f"Rs. {amount} withdrawn successfully!")

        elif choice == "4":
            print("Logged out successfully.\n")
            break

        else:
            print("Invalid choice. Please try again.")


# Main Program

while True:
    print("\n WELCOME TO SIMPLE ATM SYSTEM ")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        register()
    elif option == "2":
        user = login()
        if user:
            atm_menu(user)
    elif option == "3":
        print("Thank you for using ATM System!")
        break
    else:
        print("Invalid choice. Try again.")
