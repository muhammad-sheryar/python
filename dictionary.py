#Python Dictionary -> {Key: Value} Pair


capitals = {"USA"    : "Washington DC",
            "India"  : "Dehli",
            "China"  : "Beijing",
            "Russia" : "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("US"))

# if capitals.get("Japan"):
#     print("That capital's Exist!")
# else:
#      print("That capital doesn't Exist!")
     
# capitals.update({"Germany" : "Berlin"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# values = capitals.values()
items = capitals.items()
print(items)


for key, value in capitals.items():
    print(f"{key} : {value}")