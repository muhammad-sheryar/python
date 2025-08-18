#Python Multiple Inheritance -> Inherit from more than one parent class C(A,B)
#       Multilevel Inheritance -> Inherit from parent which inherit from another parent C(B) <- B(A) <- A

class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"This {self.name} is Eating.")
    
    def sleep(self):
        print(f"This {self.name} is Sleeping.")
        
class Prey(Animal):
    
    def flee(self):
        print(f"This {self.name} is Fleeing.")

class Predator(Animal):
    
    def hunter(self):
        print(f"This {self.name} is Hunting.")
    

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nimo")

rabbit.flee()

