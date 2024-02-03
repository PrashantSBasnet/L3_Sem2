"""Data types: 
- The type of value a variable has
- Way of classifying and categorizing different types of data
- Each data types has specific characteristics and operations that can be performed on it

Built-in Python data types: 
1. Text Type: str
2. Numeric Types: int, float, complex
3. Sequence Types: list, type, range
4. Mapping Type: dict
5. Set Types: set, frozenset
6. Boolean Type: bool
7. Binary Types: bytes, bytearray, memoryview
8. None Type: NoneType

"""

val = "A placeholder to store"
print (type(val))

d1 = 10   #int
d2 = 10.5 #float
d3 = 5j   #complex
d4 = ["IT", "FODs", "Multimedia", "I don't know"]   #list
d5 = ("IT", "FODs", "Multipedia", "I don't know")   #tuple
d6 = range(10)
d7 = {"subject":"FODs", "level": 3}    #dictionary
d7 = frozenset({"maths", "science", "geography"})
d8 = False #bool

d9 = b"Somevalue"  #bytes
d10 = bytearray(5)  #byte array
d11 = memoryview(bytes(5)) #memoryview
d12 = None   #NoneType


"""differences between list and tuple
List                                                     
- Mutable  (meaning: its state can be modified after it is created)                                               
- methods like .append(),.remove() can be used to mofidy elements in a list after its creation

Tuples
- Immutable (meaning: its state cannot be modified after it is created)
- Cannot add, remove or modify elements in tuple after its creation


Frozenset 
- immutable version of a set (Set is an unordered collection of unique elements)
- Once a frozenset is created, you cannot add/remove elements from it

Python bytes
-A sequence of integeges in the range of 0-255
-Immutable sequence data type (meaning: once bytes object is created, it cannot be changed)
-Used for handling binary datatpes
-Faster to process than text datatypes (usage: ideal for reading binary files or sending data over a network)

Bytearray
- Mutable sequence of bytes
- Can be modified after creation
- Usage: Scenarios where mutable sequence of bytes are needed, such as in low-level programming, networking, or when dealing with binary data that requires modification

MemoryView 
-  a built-in object that provides a view of the memory underlying a given object, such as bytes.
- It allows you to access and manipulate the raw memory of an object without making a copy. 
- When used with bytes, memoryview provides an efficient way to work with the underlying byte data.

None
- special constant the represents the absence of a value or a null value
"""

print (type(d3))