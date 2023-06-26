# we use this to module to randomly select the computer_choice
import random


def rock_paper_scissors():
    print("Enter 'r' for rock, 'p' for paper, or 's' for scissors.")
    # user can play the game ib the terminal, .lower is used to covert the input to lower case
    # ensuring uppercase letter don't affect the comparison.
    user_choice = input("Let's play: ").lower()
    computer_choice = random.choice(['r', 'p', 's'])


    if computer_choice == 'r':
        print("Computer chooses rock!")
    elif computer_choice == 'p':
        print("Computer chooses paper!")
    else:
        print("Computer chooses scissors!")

    if user_choice == computer_choice:
        print("It's a tie!")
    # you can have as many elif statements as you like on one line. 
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
        print("You win!")
    else:
        print("You lose!")


rock_paper_scissors()