import os, sys, random, json, getpass

choices = ["rock","r","paper","p","scissors","s"]
valid_choices = ["rock", "paper", "scissors"]
mapping = {"r": "rock", "p": "paper", "s": "scissors"}

def load_lb():
    try:
        with open("leaderboard.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
        
def save_lb(leaderboard):
    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file, indent=4)

def display_lb(leaderboard):
    if not leaderboard:
        print("No scores yet!")
        return
    print("Leaderboard:")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for player, wins in sorted_leaderboard:
        print(f"{player}: {wins} wins")
        
def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hello, this is a game Rock, Paper, Scissors made in Python!\nEnjoy the game!\n")
    input("Press Enter to start the game...\n")
    print ("Choose your game mode:\n1. Single Player (vs Computer)\n2. Two Players\n3. Leaderboard\n4. Exit\n")
    try:
         mode = int(input("Enter 1, 2, 3 or 4: "))
         if mode not in [1, 2, 3, 4]:
             raise ValueError
    except ValueError:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
        sys.exit(1)
    if mode == 1:
        print("You chose Single Player mode.")
    elif mode == 2:
        print("You chose Two Players mode.")
    elif mode == 3:
        print("You chose to view the Leaderboard.")
        display_lb(load_lb())
        input("Press Enter to continue...")
        return welcome()
    elif mode == 4:
        print("You chose to exit the game.\nThanks for playing!\nGoodbye!")
        sys.exit(0)
    return mode

def invalid_choice():
    print("Invalid choice. Please choose Rock, Paper, Scissors (or r, p, s).")
    sys.exit(1)

def game(mode, leaderboard):
    if mode == 1:
        player_name = "Player"
        p1 = input("[Player] Please choose Rock, Paper, Scissors (or r, p, s): ").lower()
        if p1 not in choices:
            invalid_choice()
        if p1 in mapping:
            p1 = mapping[p1]
        # cc = computer choice
        p2 = random.choice(valid_choices)
        computer_name = "Computer"
    elif mode == 2:
        while True:
            player_name = input("Enter Player 1 name: ")
            if player_name.strip():
                break
            print("Name cannot be empty. Please try again.")
        p1 = getpass.getpass(f"[{player_name}] Please choose Rock, Paper, Scissors (or r, p, s): ").lower()
        if p1 not in choices:
            invalid_choice()
        if p1 in mapping:
            p1 = mapping[p1]
        while True:
            computer_name = input("Enter Player 2 name: ")
            if computer_name.strip():
                break
            print("Name cannot be empty. Please try again.")
        p2 = getpass.getpass(f"[{computer_name}] Please choose Rock, Paper, Scissors (or r, p, s): ").lower()
        if p2 not in choices:
           invalid_choice()
        if p2 in mapping:
            p2 = mapping[p2]
    else:
        print("Invalid mode selected. Please restart the game.")
        sys.exit(1)
    return [p1, p2, player_name, computer_name]
    
def determine_winner(players, mode, leaderboard):  # Line 63
    p1, p2, player_name, computer_name = players  # Fix: Unpack names
    if mode == 1:
        print(f"\nPlayer chose: {p1.capitalize()}\nComputer chose: {p2.capitalize()}")
    elif mode == 2:
        print(f"\n[{player_name}] chose: {p1.capitalize()}\n[{computer_name}] chose: {p2.capitalize()}")
    if p1 == p2:
        print("\nIt's a tie!")
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        print(f"\nPlayer 1 wins!\n{p1.capitalize()} beats {p2.capitalize()}!")
        leaderboard[player_name] = leaderboard.get(player_name, 0) + 1  # Fix: Update leaderboard
    else:
        print(f"\n{'Computer' if mode == 1 else computer_name} wins!\n{p2.capitalize()} beats {p1.capitalize()}!")
        leaderboard[computer_name] = leaderboard.get(computer_name, 0) + 1  # Fix: Update leaderboard
    save_lb(leaderboard)  # Fix: Save leaderboard

def repeatOrexit():
    print("Nice game!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "yes" or play_again == "y":
        return True
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thanks for playing! Goodbye!")
        return False

def main():
    leaderboard = load_lb()
    mode = welcome()
    while True:
        if mode == 3:  # Handle leaderboard mode
            mode = welcome()
            continue
        play_again = True
        while play_again:
            players = game(mode, leaderboard)
            os.system('cls' if os.name == 'nt' else 'clear')
            determine_winner(players, mode, leaderboard)
            play_again = repeatOrexit()
        mode = welcome()

if __name__ == "__main__": 
    main()