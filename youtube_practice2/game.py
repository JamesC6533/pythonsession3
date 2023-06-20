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
