
def sum(a, b):
    return (a + b)
    
def subtract(a,b):
    print (a-b)
    

y = subtract(4,3)

print (y)


---------------------------------------------

str1 = 'global variables'

def some_function():
    str1 = 'local variables'
    print (str1)
    
def another_fn():
    str2 =str1 #from global scope
    print (str2)

    
some_function()
another_fn()

print(str1)
print(str2)

---------------------------------------------

value = input("Enter a number")
value2 = input("Enter another number")

def newFunction(value, value2):
    return value+value2
    
sum = newFunction(value,value2)
print (sum)


---------------------------------------------

def myfunc(): 
    x =100
    
    def innerFunc():
        print(x)
    
    innerFunc()
    
    
myfunc()




x =100

def myfunc(): 
     
    def innerFunc():
        print(x)
    
    innerFunc()
    
myfunc()

----------------------------------------


x = 20

# Defining a function named add
def add():
    # Declaring x as a global variable inside the function
    global x
    # Incrementing the value of x by 23
    x = x + 23
    # Printing the updated value of x
    print(x)

# Calling the add function
add()



----------------------------------------

y = 10
def fun1():
    print(y)
    z = y +10
    print (z)
fun1()


----------------------------------------
# the global keyword is used to modify a variable outside of the current scope, typically referring to a variable defined at the top-level of a script or module
#  useful when you need to access and change a global variable within a function or other local scope

x = 10  # Global variable

def modify_global():
    global x
    x = 20  # Modifying the global variable

print("Before modification, x is:", x)
modify_global()
print("After modification, x is:", x)
-------------------------------------------

def fun1():
    x=10
    def innerfun():
        nonlocal x
        x=x+10
        print(x)
    innerfun()

fun1()

----------------------------------------

x =10
def fun1():
    def innerfun():
        global x
        x=x+10
        print(x)
    innerfun()

fun1()

----------------------------------------

x = 20
def add():
    global x
    x = x+23
    print (x)
    def inner():
        global x
        x=x*78
        print(x)
    inner()
add()

----------------------------------------

x = 20
def add():
    global x
    x = x+5
    print (x) #Output:25
    def inner():
        global x # x=25
        x=x+15 #x=25+15
        print(x) #Output x=40
    inner()
add()
print(x) #value has been changed x=40
