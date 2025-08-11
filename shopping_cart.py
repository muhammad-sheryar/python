#Shopping Cart 

foods = []
quant = []
prices = []
total = 0

while True:
    food = input("Enter a Food To Buy (q to Quit): ")
    if food.lower() == "q":
        break
    else:
        quantity = int(input("Enter Quantity: "))
        price = float(input(f"Enter the Price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        quant.append(quantity)
        
print()
print("----- Your Cart -----")

for food in foods:
    print(food, end=" ") 
    
for price in prices:
    total += price * quantity

print()    
print(f"Your Total is: ${total}")