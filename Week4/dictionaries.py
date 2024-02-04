"""
Dictionary

Items are preserved in key:value pairs
{key,value} ---> {1, "Name1"}, {2, "Name2"}, {3, "Name3"}

Dictionaries cannot have two items with the same key. Duplicates are not allowed in the key. Values can be duplicate. 
   {1, "Ram"}, {2, "Ram"}, {3, "Shyam"}  ---> Allowed
   {1, "Ram"}, {1, "Ram"} ---> Not Allowed

Dictionary items are ordered (from 3.7 version onwards), changeable and do not allow duplicates

Ordered - when you iterate through a dictionary, the order of items will be the same as they were added to the dictionary

Unordered - The elements can be arranged in any order, and there is no guarantee that the order will be maintained
           - does not involve using indices because there is no predetermined position for each item.
"""


thisdict ={ "id": 1, "name": "ShivNath"}
print (thisdict)

#attempting to insert a key that already exists, the new value will simply overwrite the existing one
thisdict ={ "id": 1, "name": "RamNath"}
print (thisdict)



thisdict = {
    "id":1, 
    "name":"Ram"
}

print (thisdict["name"])  #accessing via key

#order is maintained
dict1= {1:"One", 2:"Two", 3:"Three"}
print(dict1)  #is printed in the same order as it was inserted


#using dict() constructor to 
dict3 = dict(id=1, name="Using Constructor")
print(dict3)


#values can be duplicates
dict2 ={1:"Apple", 2:"Ball", 3:"Cat", 4:"Apple"}
print(dict2)

#length
print(len(dict2))


#values in dictionary can be of any data types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "mileage": 12.34
  "colors": ["red", "white", "blue"]
}


#data type of dictionary?
#Python defines dictionaries as objects with the data type 'dict'
print(type(thisdict))




