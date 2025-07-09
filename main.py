import os
import sys
import random

choices = ["rock","r","paper","p","scissors","s"]
valid_choices = ["rock", "paper", "scissors"]
mapping = {"r": "rock", "p": "paper", "s": "scissors"}

def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hello, this is a game Rock, Paper, Scissors made in Python!\nEnjoy the game!\n")
    input("Press Enter to start the game...")
    print ("\nChoose your game mode:\n1. Single Player (vs Computer)\n2. Two Players")
    try:
         mode = int(input("Enter 1 or 2: "))
         if mode not in [1, 2]:
             raise ValueError
    except ValueError:
        print("Invalid choice. Please enter 1 or 2.")
        sys.exit(1)
    print(f"You chose {'Single Player' if mode == 1 else 'Two Players'}.")    
    return mode

def invalid_choice():
    print("Invalid choice. Please choose Rock, Paper, Scissors (or r, p, s).")
    sys.exit(1)

def game(mode):
    if mode == 1:
        # pc = player choice
        p1 = input("[Player] Please choose Rock, Paper, Scissors (or r, p, s): ").lower()
        if p1 not in choices:
            invalid_choice()
        if p1 in mapping:
            p1 = mapping[p1]
        # cc = computer choice
        p2 = random.choice(valid_choices)
    elif mode == 2:
        # p1 = player 1 choice
        p1 = input("[Player 1] Please choose Rock, Paper, Scissors (or r, p, s): ").lower()
        if p1 not in choices:
            invalid_choice()
        if p1 in mapping:
            p1 = mapping[p1]
        # p2 = player 2 choice
        p2 = input("[Player 2] Please choose Rock, Paper, Scissors (or r, p, s): ").lower()
        if p2 not in choices:
           invalid_choice()
        if p2 in mapping:
            p2 = mapping[p2]  
    else:
        print("Invalid mode selected. Please restart the game.")
        sys.exit(1)
    players = [p1, p2]
    return players

def determine_winner(players, mode):
    p1 = players[0]
    p2 = players[1]
    if mode == 1:
        print(f"\nPlayer chose: {p1.capitalize()}\nComputer chose: {p2.capitalize()}")
    elif mode == 2:
        print(f"[Player 1] chose: {p1.capitalize()}\n[Player 2] chose: {p2.capitalize()}")
    if p1 == p2:
        print("\nIt's a tie!")
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        print(f"\nPlayer 1 wins!\n{p1.capitalize()} beats {p2.capitalize()}!")
    else:
        if mode == 1:
            print(f"\nComputer wins!\n{p2.capitalize()} beats {p1.capitalize()}!")
        else:
            print(f"\nPlayer 2 wins!\n{p2.capitalize()} beats {p1.capitalize()}!")

def repeatOrexit():
    print("Nice game!")
    call = input("Play again? (yes/no): ").lower()
    if call == "yes" or call == "y":
        return True
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thanks for playing! Goodbye!")
        return False

def main():
    mode = welcome()
    call = True
    while call:
        players = game(mode)
        os.system('cls' if os.name == 'nt' else 'clear')
        determine_winner(players, mode)
        call = repeatOrexit()

if __name__ == "__main__": 
    main()