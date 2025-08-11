#Python String Methods

# name = input("Enter Your Full Name: ")
# phone_number = input("Enter Phone Number: ")

# result = len(name)
# result = name.find("Sher")
# result = name.rfind("o")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# result = phone_number.replace("-"," ")
# print(help(str))

# print(result)

#Exercise

username = input("Enter a Name: ")


if len(username) > 12:
    print("Can't be more than 12 Characters!")
elif not username.find(" ") == -1:
    print("Can't Contain Spaces!")
elif not username.isalpha():
    print("Can't Use Digits!")
else: 
    print(f"Welcome {username}")
