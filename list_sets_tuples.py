#Python Collection -> Single Variable used to store multiple values
# List   = [] Ordered & Changeable Duplicates ok
# Set    = {} Unordered & Immutable, Add Remove Ok But No Duplicates
# Tuples = () Ordered & Unchangeable. Duplicates Ok. Faster

#List Slicing Same Like Strings
fruits = ["apple","banana","orange","coconut"]

# print(fruits[::-1])

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits[0] = "Pineapple"
# fruits.append("Pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("apple"))



# for fruit in fruits:
#     print(fruit)

#Sets
fruits = {"apple","banana","orange","coconut","coconut"}

# print(dir(fruits))
# print(help(fruits))
# print(fruits[0]) #create an error

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()

# print(fruits)

#Tuples

fruits = ("apple","banana","orange","coconut","coconut")

# print(dir(fruits))
# print(help(fruits))

print(fruits.index("apple"))
print(fruits.count("apple"))
print(fruits)

for fruit in fruits:
    print(fruit)