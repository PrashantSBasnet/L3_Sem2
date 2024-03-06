class Vehicle: 
    
    def engineStart(self):
        print ("Vehicle's engine has started!!")
        
    def recharge(self):
        print ('Vechicle is recharging!!')

class Car(Vehicle): 
    
    def engineStart(self):
        print ("Car's engine has started!!")
        

obj1 = Vehicle() #parent
obj1.engineStart()

obj2 = Car() #child
obj2.engineStart()

obj2.recharge() 