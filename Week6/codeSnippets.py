'''example1'''
class FirstClass: 
    
    def config(self):
        print ('Hello world')
        
firstClassObj = FirstClass()
firstClassObj.config()

'''example2'''

class FirstClass: 
    
    def config(self):
        print ('Hello world')
        
firstClassObj = FirstClass()

FirstClass.config(firstClassObj)


'''example3'''
class Student: 
    #attributes/propoerties
    name = 'Kanchana'
    address = 'Tinkune'
    
    #behaviours/methods
    def getDetails(self):
        print (self.name, self.address)
        

studentObj1 = Student()
studentObj1.getDetails()


'''example4'''
class University: 
    def __init__(self, collegeName):
        self.collegeName= collegeName
        
    def getCollegeName(self):
        return self.collegeName

obj1 = University('TheBritishCollege')
print (obj1.getCollegeName())


'''example5'''
class Student:
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age

    def birthday(self):
        self.person_age += 1

    def getName(self):
        return self.person_name
     

fresher = Student('Sameer', 19)
print (fresher.person_name)    #works ok because it is public         


'''accessing private variables'''

class Student:
    def __init__(self, name, age):
        self.__person_name = name  # Private variable
        self.person_age = age

    def birthday(self):
        self.person_age += 1

    def getName(self):
        return self.__person_name

fresher = Student('Sameer', 19)
print (fresher.__person_name) #it will give attribute error becuase __person_name is private

'''we can access private variables through methods'''
class Student:
    def __init__(self, name, age):
        self.__person_name = name  # Private variable
        self.person_age = age

    def birthday(self):
        self.person_age += 1

    def getName(self):
        return self.__person_name

fresher = Student('Sameer', 19)
print(fresher.getName())  # Accessing private variable through a method

--------------------------------------------------------------
class Shape:
    shape = 'Rectangle'
    area = 10

    def __init__(self, shape, area):
        self.shape=shape
        self.area = area

    def giveDetails(self):
        print (self.shape, self.area)

obj1 = Shape('Circle', 23)
obj1.giveDetails()

obj2 = Shape('Square', 240)
obj2.giveDetails()

   
   
