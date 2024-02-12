
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