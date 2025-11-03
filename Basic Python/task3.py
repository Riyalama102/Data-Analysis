# Task: Update calculator task using match keyword.

while True:
    print("\nSimple Calculator (using match)")
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
            print("Result:", a + b)

        case 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a - b)

        case 3:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a * b)

        case 4:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Division by zero")

        case 5:
            print("Exiting Calculator...")
            break

        case _:
            print("Invalid choice! Try again.")


# Task: Find the Day name from the Day number.

day_number = int(input("Enter day number (1-7): "))

match day_number:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid day number! Please enter between 1 and 7.")
