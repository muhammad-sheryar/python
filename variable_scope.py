#Python Variable Scope -> Where a variable is visble and accessible
#Scope Resolution -> (LEGB) Local (Check In Own House) -> Enclosed(Neighbour's House) -> Global(Check in area) -> Built-In(Check in Modules)

# def func1():
#     print(x)
    
# def func2():
#     print(x)
    
# x = 3 
# func1()
# func2()

from math import e

def func1():
    print(e)

e = 3
func1()