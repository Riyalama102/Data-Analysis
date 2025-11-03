#Deadline: Tuesday
# 1. Program to check if a number is positive or negative (using nested if)

num = int(input("Enter a number: "))

if num > 0:
        print("Positive")
else:
        print("Negative")


# 2. Program to check whether a number is even or odd (using modulus and ternary operator)
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Program to check whether a person is eligible to vote (using simple flag variable)

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 4. Program to compare two numbers and print the larger one (using max function)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

larger = max(a, b)
print("Larger number:", larger)

# 5. Program to check if a number is divisible by 5 (using remainder variable)

num = int(input("Enter a number: "))
remainder = num % 5

if remainder == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# 6. Program to check whether a number is positive, negative, or zero (using elif chain)

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 7. Program to assign grades (using multiple conditions)

marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

# 8. Program to check whether a character is vowel or consonant (using list)

ch = input("Enter a character: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']

if ch in vowels:
    print("Vowel")
else:
    print("Consonant")

# 9. Program to find the largest among three numbers (using nested if)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# 10. Program to check if a number is divisible by both 3 and 5 (using logical AND)

num = int(input("Enter a number: "))
if (num % 3 == 0) and (num % 5 == 0):
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

# 11. Program to check whether a given number is a two-digit number (using range check)

num = int(input("Enter a number: "))

if 10 <= abs(num) <= 99:
    print("Two-digit number")
else:
    print("Not a two-digit number")

# 12. Program to check whether a character is uppercase, lowercase, digit, or special character

ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("Uppercase")
elif 'a' <= ch <= 'z':
    print("Lowercase")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special character")

# 13. Program to determine if a person can donate blood (age ≥ 18 and weight ≥ 50)

age = int(input("Enter age: "))
weight = int(input("Enter weight: "))

if age >= 18 and weight >= 50:
    print("Eligible to donate blood")
else:
    print("Not eligible to donate blood")


# 14. Program to check whether a triangle is equilateral, isosceles, or scalene

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# 15. Program to calculate electricity bill based on units

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Electricity Bill: Rs.", bill)

# 16. Program to check whether a student passed or failed (marks ≥ 40 = pass)

marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 17. Program to determine ticket price based on age

age = int(input("Enter age: "))

if age < 12:
    price = 100
elif age <= 18:
    price = 150
else:
    price = 200

print("Ticket Price: Rs.", price)

# 18. Program to check whether a person is eligible for a driving license (age ≥ 18)

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

# 19. Program to check whether a number is prime or not (using flag method)
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")


