#Try exectuting statement/s separately so that you can understand their functionalities

#The ord() function in Python returns the Unicode code point for a given character.
print (ord('a'))
print (ord('0'))


#The chr() function in Python is the inverse of the ord() function. It takes an integer representing a Unicode code point and returns the corresponding character.
print (chr(65))


tup2=(10,) #to create tuple with one element

#converting list into tuple
sampleList = [1,3,4, 'Ram']
sampleTupl = tuple(sampleList)

#access elements of a tuple using indexing, with positive indices starting from 0 for the first element and negative indices starting from -1 for the last element
print (sampleTupl[-1])

#access elements giving range
print (sampleTupl[1:3])

print (sampleList[1:3])