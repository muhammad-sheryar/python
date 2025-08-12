#Python Default Arguememnts 

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500, 0.1))

import time

def count(stop, start=0):
    for x in range(start, stop):
        print(x)
        time.sleep(1)
    print("Done!")
    
count(10)