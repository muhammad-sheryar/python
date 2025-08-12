#Concession Stand

menu = {"Pizza"   : 3.00,
        "Nachos"  : 4.50,
        "Popcorn" : 6.00,
        "Fries"   : 2.50,
        "Chips"   : 1.00,
        "Pretzel" : 3.50,
        "Soda"    : 3.00,
        "Lemonade": 4.25}

cart = []
total = 0

print("------Menu------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
       
print("----------------")

while True:
    food = input("Select an Item (q to Quit): ").capitalize()
    if food.lower() == "q":
        break 
    elif menu.get(food) is not None:
        cart.append(food)

print("------YOUR ORDER------")        
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")
        

        






