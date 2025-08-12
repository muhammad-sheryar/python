#python Number Guessing Game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True 

print("Python Number Guessing Game")
print(f"Select Number Between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter Your Guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print("Number Out Of Range!")
            print(f"Please Select a Number Between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too Low! Try Again!")
        elif guess > answer:
            print("Too High! Try Again!")
        else:
            print(f"CORRECT! The Answer was {answer}")
            print(f"Number of Guesses: {guesses}")
            is_running = False
    else:
        print("Invalid Guess!")
        print(f"Please Select a Number Between {lowest_num} and {highest_num}")
        

# print(answer)
