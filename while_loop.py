#Python While loop -> Continues Until Condition remains True 

# name = input("Enter Your Name: ")

# while name == "":
#         print("You didn't enter your name.")
#         name = input("Enter Your Name: ") #Give Chance To end loop Otherwise loop will go into infinity
        
# print(f"Hello {name}!")



# age = int(input("Enter Your Age: "))

# while age < 0:
#     print("Can't be Negative!")
#     age = int(input("Enter Your Age: "))
    
# print(f"You are {age} years old.")

# food = input("Enter Food You Like (q to Quit): ")

# while not food == "q":
#         print(f"You like {food}!")
#         food = input("Enter another Food You Like (q to Quit): ")

# print("Bye!")

num = int(input("Enter Number Between 1-10: "))

while num < 1 or num > 10:
    print("Number is Not Valid!")
    num = int(input("Enter Number Between 1-10: "))
    
print(f"Your Number is {num}")