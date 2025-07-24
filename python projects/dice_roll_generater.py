import random
import os 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_dice_settings():
    while True:
        try:
            sides = int(input("Enter number of sides on the dice (e.g., 6, 8, 20): "))
            if sides < 2:
                print("dice must have at least 2 sides.")
                continue
            return sides 
        except ValueError:
            print("Please enter a valid number.")

def get_number_of_dice():
    while True:
        try:
            num = int(input("Roll 1 or 2 dice? E nter 1 or 2: "))
            if num in [1, 2]:
                return num
            print("Only 1 or 2 allowed.")
        except ValueError:
            print("Enter a number (1 or 2).")

def get_players():
    players = []
    num_players = int (input("How many players? "))
    for i in range(num_players):
        name = input(f"Enter name for player {i+1}: ")
        players.append({'name': name, 'score': 0})
        return players 
    
def roll(player_name, num_dice, sides):
    print(f"\n{player_name}'s turn:")
    input("press enter to roll...")

    total = 0
    for i in range(num_dice):
        roll = random.randint(1, sides)
        print(f"dice {i+1}: {roll}")
        total += roll
    print(f"Total rolled: {total}")
    return total

def play_game():
    clear_screen()
    print("🎲 Welcome to the Multiplayer Dice Game 🎲\n")

    sides = get_dice_settings()
    num_dice = get_number_of_dice()
    players = get_players()

    while True:
        clear_screen()
        print("Rolling dice for all players...\n")

        for player in players:
            score = roll(player['name'], num_dice, sides)
            player['score'] += score
        
        print("\nCurrent Scores:")
        for player in players:
            print(f"{player['name']}: {player['score']}")

        again = input(f"\nPlay another round? (y/n): ").lower()
        if again not in ['y', 'yes']:
            print(f"\nFinal Scores:")
            for players in players:
                print(f"{player['name']}: {player['score']}")
            print("\nThanks for playing!  ")
            break

if __name__ == '__main__':
    play_game()
            










