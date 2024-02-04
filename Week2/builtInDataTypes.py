
# Online Python - IDE, Editor, Compiler, Interpreter
#Built in data types
#List, Tuple, Set, Dictionary

"""List
-allows duplicates
-order of the elements is maintained
-mutable (their elements can be modified using various methods like append(), remove())
-supports heterogenous elements 
-dynamic (grows and shrinks in size)
-supports indexing and slicing
"""
#defining a list
theList = ["cat", "dog", "elephant"]
print (theList)

#using list() constructor
theList3 = list(("cat", "dog", "elephant"))
print(theList3)


theList2 = ["apple", "apple", None, 13, 53.55]
print (theList2)

#insert
theList2.insert(13, "Thirteen")
print (theList2)

#append
theList2.append("moreValues")
print(theList2)

#remove
theList2.remove("moreValues")
print(theList2)

#length
print (len(theList2))

#concatenation
concatList = theList+theList2
print (concatList)

#common methods: append(), extend(), insert(), remove(), pop(), index(), count()
print(concatList.clear())


#--------------------------------------------------------------------------------------

#Tuples
#stores multiple items in a single variable
#ordered - defined order and it will not change
#unchangeable - the items cannot be changed, added or removed after the tuple has been created
#allowsDuplicates
#can contain different datatypes
theTuple = ("Kathmandu", "Lalipur", "Bhaktapur")
sampleTuple = ("Banepa")
theTuple2 = ("abc", 32, True, 32)
print (theTuple)

#length
print(len(theTuple))


#--------------------------------------------------------------------------------------



