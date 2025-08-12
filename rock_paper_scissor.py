#Python Rock Paper Scissors


import random
options = ("rock", "paper", "scissor")
running = True

while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors): ")
        

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissor":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissor" and computer == "paper":
        print("You Win!")
    else:
        print("You Lose!")
        
    play_Again = input("Play Again? (y/n): ").lower()
    if not play_Again == "y":
        break
    
print("Thanks For Playing")