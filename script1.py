
# print(dir())

# def favourite_food(food):
#     print(f"Your Favourite Food is {food}")


# def main():
#     print("This is Script1.")
#     favourite_food("Pizza")
#     print("Good Bye!")

# if __name__ == '__main__':
#       main()
      
      
      
# print(__name__)

def greet(name):
    print(f"Hello, {name}!")

if __name__ == '__main__':
    # This code will only run when my_module.py is executed directly
    print("Running my_module.py directly!")
    greet("World")

# This code will always run, whether imported or executed directly
print("This line always runs.")

