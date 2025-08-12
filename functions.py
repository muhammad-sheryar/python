#Python Functions -> Reusable Code

# def happy_birthday(name, age):
#     print(f"Happy Birthday! {name}")
#     print(f"You are {age} years old.")
    
# happy_birthday("Sherry", 20) 
# happy_birthday("Ali", 25) 

# def display_invoice(username, amount, due_date):
#     print(f"Hello! {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
    
# display_invoice("sherry", 25, "01/01")

# def add(a,b):
#     return f"Sum is: {a+b}"

# c = add(5,6)
# print(c)

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}!"

full_name =create_name("sherry","bro")
print(full_name)