# File Handling

# The flow for file handling is
# Open the file => open(file_path, open_mode)
# r, w, a
# r ( read mode ) => Read the file. It throws error if the file is not present
# w ( write mode ) => Write in the file erasing the previous content. It creates an empty file if the file is not present
# a ( append mode ) => Write in the file preserving the previous content. It creates an empty file if the file is not present

# Perform operation on file
# Close the file

# file = open("test1.txt","a")
# file.write("[1,2,3,4,5]")
# # We can only write either string or JSON on file
# # JSON => Javascript Object Notation
# file.close()

# file = open("test1.txt","r")
# content = file.read()
# file.close()

# print(content)

# Task: Revise the file handling and file methods and mode
# Task: Explore about JSON


# split() => Split method splits the words from a unique character and returns a list of words
# By default, split() method splits the string by space

# name = "Ujjwal Neupane abc def , ghi"
# list_of_words = name.split(",")
# print(list_of_words)


# usernames = ["Ujjwal","Abc","Ram","Shyam","Hari"]
# file = open("test1.txt","a")
# file.write(str(usernames))
# file.close()


    
# Register => ask username from user and append it in a file
# Login => read, split(), check 

username = input("Enter your username: ")
file = open("test1.txt","a")
file.write(username+"-")
file.close()

file = open("test1.txt","r")
content = file.read()
file.close()

usernames = content.split("-")
usernamel = input("Enter your username: ")
if usernamel in usernames:
    print("Login Successful")
else:
    print("Login Failed")