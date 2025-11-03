# Exception Handling

# nm1 = 5
# num2 = 0
# try:
# # print(nm1/num2)
# except:
    

# Try Except Finally

# try:
# In try block we write the part of code that may raise an error

# except:
# In except block, we write the code that is to be executed if error occurs in try block

# finally:
# The code of finally block runs even if error occurs or not. Basically it always gets executed.

# try:
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# print(num1/num2)
# except Exception as e:
# print("Error occured: ",e)
    
# try:    
# file = open("abc.txt","r")
# content = file.read()
# file.close()
# except FileNotFoundError:
# file = open("abc.txt","w")
# file.close()


list = [1,2,3,4,5]
try: 
    print(list[1:10])
    
    try:
        pass
    except:
        pass
    
except:
    print("Error: ")
    try:
        pass
    except:
        pass
    finally:
        pass
    
finally:
    pass

# Task: Update every program we have done using try except
