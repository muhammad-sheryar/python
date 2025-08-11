#Logical Operators -> Multiple Conditons

#OR

# temp = 22
# is_raising = True

# if temp > 35 or temp < 0 or is_raising:
#     print("The Outdoor Event is Cancelled!")
# else:
#     print("The Outdoor event is still scheduled.")

#AND

temp = 28
is_raising = False

if temp >=  35 and is_raising:
    print("It is Hot Outside.")
    print("It is Sunny.")

elif temp <= 0 and is_raising:
    print("It is Cold Outside.")
    print("It is Sunny.")
    
elif temp <= 28 and temp >= 0 and is_raising:
    print("It is Warm Outside.")
    print("It is Sunny.")

elif temp >=  35 and not is_raising:
    print("It is Hot Outside.")
    print("It is Cloudy.")

elif temp <= 0 and not is_raising:
    print("It is Cold Outside.")
    print("It is Cloudy.")
    
elif temp <= 28 and temp >= 0 and not is_raising:
    print("It is Warm Outside.")
    print("It is Cloudy.")    
    
    
