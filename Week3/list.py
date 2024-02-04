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

theList = ["cat", "dog", "elephant"]
print (theList)

theList2 = ["apple", "apple", None, 13, 53.55]
print (theList2)

#insert
theList2.insert(13, "Thirteen")
print (theList2)

#append
theList2.append("moreValues")
print(theList2)

#remove
theList2.remove()
print(theList2)

#length
print (len(theList2))

#concatenation
print(theList+theList2)

#common methods: append(), extend(), insert(), remove(), pop(), index(), count()



