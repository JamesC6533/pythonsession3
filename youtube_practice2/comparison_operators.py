# if the temperature is over 30, less than 10 or inbetween then it will print relevant message
temperature = 30

if temperature > 30:
    print("It's a hot day!")
elif temperature < 10:
    print("It's a cold day!")
else:
    print("It's a lovely day")

# if the length len() name is less than 3 or greater than 50 print relevant message
name = "James"

if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")




