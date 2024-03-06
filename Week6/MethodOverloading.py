class Student: 
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def sum (self,a=None,b=None,c=None):
       
       sum =0 
       
       if a!=None and b!=None and c!=None:
           sum = a+b+c
       elif a!=None and b!=None:
           sum = a+b
       else: 
           sum = a
       return sum

s1 = Student (70,80)
print (s1.sum(10,20,30))
print (s1.sum(10,20))
print (s1.sum(10))