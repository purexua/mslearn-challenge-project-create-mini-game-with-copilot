# Now I need to develop a mini-game, the programming language is python.
# Specific requirements are as follows:

# 1. Game logic

# The winner of the game is determined by three simple rules:+
# - Rock beats scissors.
# - Scissors beat paper.
# - Paper beats rock.

# 2. Game interaction considerations
# The computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors). Your game interaction will be through the console (Terminal).

# - The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# - At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# - By the end of each round, the player can choose whether to play again.
# - Display the player's score at the end of the game.
# - The mini-game must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random

def play_game():
    player_score = 0
    rounds_played = 0

    while True:
        print("\nRound", rounds_played + 1)

        # Player input
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        # Check for valid input
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        # Computer randomly chooses
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Computer chooses", computer_choice)

        # Determine winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'scissors' and computer_choice == 'paper') or
            (player_choice == 'paper' and computer_choice == 'rock')
        ):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

        rounds_played += 1

    print("\nGame Over")
    print("Total rounds played:", rounds_played)
    print("Your score:", player_score)

if __name__ == "__main__":
    play_game()