def century(year):
    # assigns the value of year // 100 to century.
    # If year is divisible by 100, the result will be the century
    century = year // 100
    # checks if the remainder of dividing the year by 100 is equal to 0.
    # This condition verifies whether the year is exactly divisible by 100
    if year % 100 > 0:
        # increments the value of century by 1
        century += 1
    return century


year = 1023
result = century(year)
print(result)
