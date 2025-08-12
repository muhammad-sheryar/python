#Python Iterables -> Loop over Objects/Collections


# numbers = (1, 2, 3, 4, 5)

# for item in reversed(numbers):
#     print(item, end="-")

# print(type(numbers))

# fruits =  {"apple", "orange", "banana", "coconut"}
    
# for fruit in fruits: #set is not reversable.
#     print(fruit)

# name = "Sherry"

# for character in name:
#     print(character, end=" ")

my_dictionary = {"A" : 1, "B" : 2, "C" : 3,}

for key, value in my_dictionary.items():
    print(f"{key}: {value}")
    
    