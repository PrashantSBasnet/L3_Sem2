#strings       
for x in "Abcdef":
    print(x)
    
print("")
str1 = "MyNameisName"
print(len(str1))    

print("is" in str1)
print ("is" not in str1)

print("")
#slicing string
print (str1[1:3])
print (str1[:3]) #staring from the start
print (str1[1:]) #all the way to the end

str2 = "Hello"
print (str2[-4:-2])   #gives substring from the 4th character from the end and ending at the 2nd character from the end (excluding character at the end index)

#modify string
print (str2.upper())  #Uppercase
print (str2.lower())  #Lowercase

str3 = " Hi There  "
print (str3.strip())  #return "Hi There"
print (str3.replace("T", "t"))

str4 ="Hello How are you"
print (str4.split(" "))

#string concatenation
x1 = "This"
x2 = "is"
print (x1 +" "+ x2)

#format() method to insert numbers into string
id = 1 
name = "Name"
toBePrinted= "The id of Name is {}"
print (toBePrinted.format(id))

address ="Thapatali"
rollNo= 23
output= "The id of {} is {}, rollNo is {}, and address is {}"
print (output.format(name,id,rollNo,address))

print("")
#Escape characters
print ("She said,\"I can understand, but..\" He stood there listening..")

# \'    Single Quote
# \\    Backslash
# \n    new Line
# \r    Carriage Return
# \t    tAB
# \b    Backspace
# \f    FormFeed
# \ooo  Octal value
# \xhh  Hex value

"""
Strings methods 

capitalize()	    Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()    	    Returns true if the string ends with the specified value
lower()	            Converts a string into lower case
replace()	        Returns a string where a specified value is replaced with a specified value
split()	        Splits the string at the specified separator, and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
translate()	        Returns a translated string
upper()	            Converts a string into upper case

"""
