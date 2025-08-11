#Python Temperatur Conversion

unit = input("Enter Unit Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the Temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The Tempertaure in Fahrenheit is: {temp}F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The Tempertaure in Celsius is: {temp}C")
else:
    print(f"{unit} is Invalid Unit!")