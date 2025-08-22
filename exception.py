#Python -> An event that interrupts the flow of a program

try:
    
    number = int(input("Enter a Number: "))

    print(1/number)

except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enters Only Numbers plz!")

# except Exception:
#     print("Something Went Wrong!")

finally:
    print("Do some cleanup here!")