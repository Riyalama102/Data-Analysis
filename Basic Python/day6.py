# Lambda Function - Function in one line. lambda keyword is used to define a lambda function

x = 10
y = 2
def add(x,y):
    print(x+y)

add = lambda x,y : x+y
print(add(10,2))


x = 10
y = 2
def add(x,y):
    print(x+y)

add = lambda x,y,name : x+y+name
print(add('10','2','Riya'))