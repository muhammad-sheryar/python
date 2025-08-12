#Python Arbitary Arguments *args **kwargs

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(5, 8, 3))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr", "spongebob", "Harold", "Squarepants")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print({key : value})

# print_address(street="123 Fake Street", city="Detroit", state="MI", zip="1234" )

#Exercise

def shipping_label(*args,**kwargs):
    
    for arg in args:
        print(arg, end=" ")
        
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    
    if 'apt' in kwargs:
        print(f"{kwargs.get('street')}")
        
    elif "pobox" in kwargs:
        print(f"{kwargs.get('pobox')}")
        
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('city')} {kwargs.get('state')}")
    
    
shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake Street",
               city="Detroit",
               state="MI",
               zip="1234",
               pobox="8547")