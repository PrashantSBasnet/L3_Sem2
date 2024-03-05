
'''Duck Typing'''
class Cat:
    def speak(self):
        return "Meow!"

class Mouse:
    def speak(self):
        return "Squeak!"

class Animal:
    def make_sound(self, animal):
        return animal.speak()
 
#creating instanct   
tom = Cat()
jerry = Mouse()

animal = Animal()

print(animal.make_sound(tom))
print(animal.make_sound(jerry))