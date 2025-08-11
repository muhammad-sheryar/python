#Input -> Take Input From User
#Can't operate differenct data types

# name = input("What is your Name?: ")
# age = int(input("How old are you?: "))

# age += 1

# print(f"Hello {name}!")
# print("Happy Birthday!")
# print(f"You are {age} years old!")

#Excercise

# length = int(input("Enter the length: "))
# width = int(input("Enter the width: "))
# area = length * width

# print(f"Area is: {area}cm²") #alt + 0178 -> super script

#Exercise

# item =  input("What item would you like to Buy?: ")
# price = float(input("What is Price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity

# print(f"You have Bought{item} * {quantity}")
# print(f"Your Total is: ${total}")

#Madlibs Game
#Word Game Where you create story
#By filling in the blanks with random words

adjective1 = input("ENter an Adjective: ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an Adjective: ")
verb1 = input("Enter a verb (ending with ing):")
adjective3 = input("Enter an Adjective: ")


print(f"Today i went to a {adjective1} zoo.")
print(f"In an exhibit,  I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
(f"I was {adjective3}")