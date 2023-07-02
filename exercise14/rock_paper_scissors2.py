import random


##users choice
def mychoice(choice):
    if choice == "R":
        return "Rock"
    elif choice == "P":
        return "Paper"
    elif choice == "S":
        return "Scissors"

    # computer's choice


def computerchoice(choice):
    if choice == 0:
        return "Rock"
    elif choice == 1:
        return "Paper"
    elif choice == 2:
        return "Scissors"


# determine winner
def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (
            user_choice == "Paper" and computer_choice == "Rock") or (
            user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"


# play game
def play_game():
    user_choice = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").upper()
    user_choice = mychoice(user_choice)

    computer_choice = random.randint(0, 2)
    print("Random int was ", computer_choice)
    computer_choice = computerchoice(computer_choice)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    result = winner(user_choice, computer_choice)
    print(result)


play_game()