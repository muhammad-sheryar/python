#Python Slot Machine

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    
    return [random.choice(symbols) for _ in range(3)]
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        if row[0] == "🍉":
            return bet * 4
        if row[0] == "🍋":
            return bet * 5
        if row[0] == "🔔":
            return bet * 10
        if row[0] == "⭐":
            return bet * 20
        
    return 0
        
    

def main():
    balance = 100
    
    print("***************")
    print("Welcome To Python Slot Machine!")
    print("***************")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("***************")
    
    while balance > 0:
        print(f"Current Balance: ${balance}")
        bet = input("Place Your Bet: ")
        
        if not bet.isdigit():
            print("Enter Valid Number!")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient Funds!")
            continue
        
        if bet <= 0:
            print("Bet must be Greater than 0!")
            continue
        
        balance -= bet
            
        row = spin_row()
        print("Spinnig...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You Won ${payout}.")
        else:
            print("Sorry You Lost this Round!")
            
        balance += payout
        
        play_again = input("Do you want to spin again? (Y/N): ")
        
        if play_again != "Y":
            break
        
    print("***************")    
    print(f"Game Over! Your Final Balance is ${balance}")
    print("***************")
    
if __name__ == '__main__':
    main()