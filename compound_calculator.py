#Python Compound Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter Principle Amount ($): "))
    if principle <= 0:
        print("Principle can't be less than Zero.")
    else:
        break
        
while True:
    rate = float(input("Enter Interst Rate: "))
    if rate < 0:
        print("Interest rate can't be less than Zero.")
    else:
        break

while True:
    time = int(input("Enter Time: "))
    if time < 0:
        print("Time can't be less than or Equal to Zero.")
    else:
        break
        
# print(principle)
# print(rate)
# print(time)

total = principle * pow((1 + rate / 100), time)
print(f"Balance After {time} years/s: ${total:.2f}")