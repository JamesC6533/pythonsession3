import random


def generate_lottery_numbers():
# the set() daya structure is used to ensure we have unique numbers once we have 6 we return the set
    numbers = set()
# while loop to generate random numbers between 1 and 50 until we have 6 unique numbers
    while len(numbers) < 6:
        number = random.randint(1, 50)
        numbers.add(number)

    return numbers


lottery_numbers = generate_lottery_numbers()
print("Lottery Numbers:", lottery_numbers)


