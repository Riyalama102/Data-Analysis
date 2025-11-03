# Syntax:
# while condition:
#       Code to be executed
# += , -=
# while keyword is used in while loop
# while loop is when we don't know the start and end value

# a=10
# while a >= 0:
#   print(a) 
#    a -= 1


while True:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number:"))
    choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for exit: "))
    match choice:
        case 1:
         print(num1+num2)
        case 2:
         print(num1-num2)   
        case 3:
          break       
        case _:
          print("Invalid input")

# break: Break can be used only in loop. When break encounters, it completely exits the loop
# continue: When continue encounters it skips the current iteration but continues the loop

list = [ x for x in range(1,10)]
for i in list:
    if i == 6:
        print("Breaking...")
        continue #break
    else:
        print(i)

# Nested If else 
a = 2
b = 9
c = 3

if a>b:
   if a>c:
      pass
   else:
      print("c is greatest.")
else:
   if b>c:
      print("b is greatest.")
   else:
      print("c is greatest.")

#NESTED LOOP

for i in range(1,6):
   for j in range(6,11):
      print(str(i) +","+ str(j)) # pass




    



 