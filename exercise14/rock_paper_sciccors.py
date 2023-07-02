# we use this to module to randomly select the computer_choice
import random


def rock_paper_scissors():
    # loop added so the game can continue past the first round
    while True:
        print("Enter 'r' for rock, 'p' for paper, or 's' for scissors.")
        # user can play the game ib the terminal, .lower is used to covert the input to lower case
        # ensuring uppercase letter don't affect the comparison.
        user_choice = input("Let's play: ").lower()
        computer_choice = random.choice(['r', 'p', 's'])

        if user_choice == 'r':
            print("You chose rock!")
        elif user_choice == 'p':
            print("You chose paper!")
        else:
            print("You chose scissors!")

        if computer_choice == 'r':
            print("Computer chose rock!")
        elif computer_choice == 'p':
            print("Computer chose paper!")
        else:
            print("Computer chose scissors!")

        if user_choice == computer_choice:
            print("It's a tie!")
        # you can have as many elif statements as you like on one line.
        elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
            print("You win!")
        else:
            print("You lose!")

        # adds a message so the user can choose to play again or not yes = play again,
        repeat = input("\nPlay again? (yes/no): ")
        if repeat.lower() != "yes":
            print("Thanks for playing!")
            # ends the loop
            break
        print()


rock_paper_scissors()