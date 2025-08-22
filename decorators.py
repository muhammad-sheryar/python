#Python Decorators -> A function that extends the behaviour of another function 
#                     w/o modifying the base function
#                     pass the base function as an argument to the decorator

def add_sprinkles(func):
    
    def wrapper(*args,**kwargs):
        print("You add Sprinkles 🥓")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("You have added fudge!")
        func(*args,**kwargs)
    return wrapper
   
@add_fudge 
@add_sprinkles    
def get_ice_cream(flavor): 
    print(f"Here is Your {flavor} 🍨")
    
    
get_ice_cream("Vanilla")