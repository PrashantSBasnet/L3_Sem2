class Student: 
    #class variable
    college = "BritishCollege"
    
    def __init__(self,name,address,uni):
        #instance variable
        self.name = name
        self.address = address
        self.uni = uni
    
    #accessors/getter because it fetches values
    def details(self):
        return (self.name, self.address, self.uni, self.college)
    
    #mutators/setters because if modifies values
    def update(self, name, address,uni):
        self.name = name
        self.address = address
        self.uni =uni
        
    #Class method
    @classmethod   
    def getCollege(cls):
        return cls.college
        
student = Student('Nischal','Thapathali','LBU')
print(student.details())

student.update('Grishma','Thapathali', 'UWE')
print(student.details())

print(student.getCollege()) #calling class method using object
print(Student.getCollege()) #calling class method using Class name