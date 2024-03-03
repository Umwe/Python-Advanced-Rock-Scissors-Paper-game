# Print newline for better formatting
print("\n")

# Print game title
print("KWIZERA AFRICA HUBERT BONAPARTE")

# Import the random module for generating random choices
import random

# Function to print debug messages
def print_debug(message):
    print(message)

# Function to get user's hand choice
def get_user_choice():
    while True:
        try:
            # Prompt user for input and convert it to an integer
            choice = int(input("Input your hand choice\n0=rock, 1=scissors, 2=paper "))
            
            # Check if the input is a valid choice
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to determine the winner of the game
def determine_winner(player, rival):
    if player == rival:
        return "draw"
    elif (player == 0 and rival == 1) or (player == 1 and rival == 2) or (player == 2 and rival == 0):
        return "win"
    else:
        return "lose"

# Function to update the remaining lives based on the game result
def update_lives(result, lives):
    if result == "lose":
        lives["You"] = max(0, lives["You"] - 1)
    elif result == "win":
        lives["Rival"] = max(0, lives["Rival"] - 1)
    return lives

# Function to display the remaining lives
def display_lives(lives):
    print(f"Lives You: {lives['You']} / Rival: {lives['Rival']}")

# Function to play the main game
def play_game():
    # Initialize lives
    lives = {"You": 3, "Rival": 3}
    
    # Mapping for choices
    choices = {0: "rock", 1: "scissors", 2: "paper"}

    while True:
        print("--------------------------------------")
        print("\nStart 'rock-scissors-paper' game")
        display_lives(lives)

        # Get user choice and generate rival choice
        user_choice = get_user_choice()
        rival_choice = random.randint(0, 2)

        print(f"My hand is {choices[user_choice]}")
        print(f"Rival's hand is {choices[rival_choice]}")

        # Determine the result of the game
        result = determine_winner(user_choice, rival_choice)

        if result == "draw":
            print("It's a draw")
        elif result == "win":
            print("You won!")
        else:
            print("You lost")

        # Update and display remaining lives
        lives = update_lives(result, lives)
        display_lives(lives)

        # Check if the game is over
        if lives["You"] == 0 or lives["Rival"] == 0:
            print("Game over.")
            while True:
                # Ask user if they want to replay
                replay = input("Do you want to replay? (Y or N): ")
                if replay.upper() == "Y":
                    lives = {"You": 3, "Rival": 3}
                    break
                elif replay.upper() == "N":
                    return
                else:
                    print("Invalid input. Please enter Y or N.")

# Call the main function to start the game
play_game()
