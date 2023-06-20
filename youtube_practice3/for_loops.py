# assigns 'item' a range of numbers from what you specify in the square brackets or range()
for item in range(5, 10):
    print(item)

# for loop for multiplying items in a list
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

#  nesting loops
# generates vales for the x coordinate
for x in range(4):
    # generates vales for the y coordinate
    for y in range(3):
        print(f'({x}, {y})')

