#Python Nested Loops -> Loop inside Loop

# for x in range(3):
#     for y in range(1, 10):
#         print(x, end=" ")
#     print()    #For next after execution of inner loop
 
row = int(input("Enter Number of Rows: "))
columns = int(input("Enter Number of Columns: "))
symbol = input("Symbol to use: ")

for x in range(row):
    for y in range(columns):
        print(symbol, end=" ")
    print()    #For next after execution of inner loop
