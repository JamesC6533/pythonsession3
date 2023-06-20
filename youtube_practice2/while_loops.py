# variable i has been given the value 1
i = 1
# python executes the next line as true as 1 is less then 5
while i <= 5:
    print(i)
    # i is incremented by 1
    i = i + 1
print("Done")

# the control then moves to the start of the while loop.
# in the second iteration i = 2 and because 2 is less then 5 our condition is still true
# this will repeat incrementing i + 1 each time until i = 6 and that's when our condition will be false
# once i = 6 the loop is terminated and done message will be printed in the terminal

i = 1
while i <= 5:
    # in this expression we can repeat a string by a number, the string will be repeated.
    print('*' * i)
    i = i + 1
print("Done")
# *
# **
# ***
# ****
# *****

# meaningful description of variables
secret_number = 9
guess_count = 0
guess_limit = 3
# gives the user 3 guess'
while guess_count < guess_limit:
    # whatever the user enters comes out as a string so we use the int function to convert to integer
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        # ends the loop if the correct answer is entered
        break
    # elif guess_count == 3:
    #         print("Game Over!")
#  if the user makes 3 incorrect guess' prints message.
else:
    print("Game over, sorry!")



command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Engine is off...")
    elif command == "help":
        print(""" 
start - to start the car 
stop - to turn off the engine 
quit - to exit 
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")











