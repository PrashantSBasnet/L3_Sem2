try: 
    print(x)
except NameError as e:
    print ('Excetion raised:' , e)
	

#--------------------------

try: 
    print(5/0)
except ZeroDivisionError as e: 
    print ('Exception Raised:',e)
    
#--------------------------

print (5/0)          #ZeroDivisionError or ArithmeticError
print (x)            #NameError
print (int('Ram'))   #ValueError


    