# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

#variables
x = 1 
y = "Apple"
z= 1.234

print ("Integer value:", x)
#print ("Integer value"+x) you cannot do this

print ("String value:" +  y)
#print ("String value:", y)
print ("Float value:", z)

#variable names are not case sensitive 

a1 = "Level3"
A1 = "Level3"

#assigning multiple values to multiple variables 
i, j, k = "Unit Vector in X-Axis", "Unit Vector in Y-Axis", "Unit Vector in Z-Axis"

#assigning single value in multiple variables 
i1=j1=k1=1 
""" 
multiline comments
these are two different variables A1 will not overwrite a1
"""

#casting
x1 = str(3) #casting to str output will be '3'
y2 = int(3) #casting to int output will remain as 3
z3 = float(3) #casting to float output will be 3.0

print (x,y,z)



"""rules for python variables
1. must start with a letter or underscore character
2. cannot start with a number
3. can only contain alpha-numberic characters and underscores
4. case sensitive-- Dog and DOG are two different variables
5. do not use python keywords as variables. 

The following styles help in maintaining readablity when there are more than one words in a variable

Camel case: myVariableName
Pascal case: MyVariableName
Snake case: my_variable_name




