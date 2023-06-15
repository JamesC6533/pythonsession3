def check_pin():
    supplied_pin = input("Enter your PIN: ")
    correct_pin = "1234"  # Hardcoded PIN, you can change it

    attempts = 3

    while attempts > 0:
        if supplied_pin == correct_pin:
            print("Success! Access granted.")
            break
        else:
            attempts -= 1
            print("Invalid PIN. You have", attempts, "attempts remaining.")
            if attempts == 0:
                print("Access denied.")
                break


