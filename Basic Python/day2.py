dict1 = {
    "name" : "Riya Lama",
    "age" : 24,
    "position" : "Student"
}
#keys, values, update, get
print(dict1.keys())
print(dict1.values())

dict1.update({"name": "ABCD"}) 
print(dict1)

#conditional statements works under the condition
#If the condition is true, then only the lines of code under conditional statements execute
#If the condition is false, the conditional statements is skiped

#IF - ELSE
#Syntax :
# if condition:
        #Lines of codes
#else:
     #Lines of codes

a=10
b=20
#if a>b:
    #print("A is greater than B.")
#else:
    #print("B is greater than A.")

#if else ladder
marks = 65
if marks >=90:
    print("A+")
elif marks >=80 and marks < 90:
    print("A")
elif marks >=70 and marks < 80:
    print("B+")
elif marks >=60 and marks < 70:
    print("B")
elif marks < 60:
    print("Fail")
else:
    print("Wrong marks")

usernames = ["Riya","ABC","DEF","GHI"]
username = input("Enter your username:")
if username in usernames:
    print("Username found in usernames.")
else:
    print("Username not found.")

user_dict = {"Riya":"Riya123","Ram":"Ram123","Sita":"Sita123"}
usernames = user_dict.keys()
passwords = user_dict.values()
print(usernames)
print(passwords)

username = input("Enter your username:")
if username in user_dict:
    print("Username found")
else:
    print("Username not found")

user_dict = {"Riya":"Riya123","Ram":"Ram123","Sita":"Sita123"}
print(usernames)
for i in usernames:
    print(i)
