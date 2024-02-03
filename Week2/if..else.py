#if...else

x = 10
if (x<11):
    print (x, "is less than 11")
    
a = 10
b = 20 
if b >a: 
    print ("b is greater than a")
elif a == b: 
    print ("a and b are equal")
else:
    print ("a is smaller than b")

#---------------------------------------
if b > a: 
    print ("b is greater than a")
else:
    print ("b is not greater than a")
    
#---------------------------------------    
#shorthand
a = 13
b = 12
if a < b: print ("a is less than b")

#one line if else
print ("b is greater") if b > a else print ("b is greater than a")

#one line if else with multiple condition 
print ("a is smaller") if a<b else print ("b is greater") if b>a else print ("they are equal")

#pass 
#used when you if statement is with no content and you want to avoid getting an error. Note: if statment cannot be empty

if b > a:
    pass

