#Sets
#stores multiple items in a single variable
#Unordered - an appear in a different order every time you use them, and cannot be referred to by index or key
#Unchangeable but items can be removed and new items can be added
#Unindexed

thisset = {"apple", "banana", "cherry"}
print(thisset)

print("")
#duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

print("")
#True and 1   False and 0  considered the same value
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

print("")
#length
print(len(thisset))


#adding item
thisset.add("banana")

#adding another set into the current set
theSet1 = {"A", "B", "C", "Cat"}
theSet2 = {"Horse", "Crocodile", "Elephant"}

theSet1.update(theSet2)
print(theSet1)
print("")

#removing
theSet1.remove("A")
print(theSet1)

#looping
for x in thisset:
    print(x)

