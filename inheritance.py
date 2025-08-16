#Python Inheritance -> Inherit Attributes and Methods from other Class

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is Eating.")
        
    def sleep(self):
        print(f"{self.name} is Sleeping.")
        
class Dog(Animal):
    def speak(self):
        print("Woof!")
    
class Cat(Animal):
    def speak(self):
        print("Meow!")
    

class Mouse(Animal):
    def speak(self):
        print("Sniff!")
    

dog = Dog("Scooby Doo!")
cat = Cat("Tom")
mouse = Mouse("Jerry")

# print(dog.name)
# print(dog.is_alive)

# cat.eat()
# cat.sleep()

# dog.speak()
# cat.speak()
