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
# generates vales for the x coordination
for x in range(4):
    # generates vales for the y coordinate
    for y in range(3):
        print(f'({x}, {y})')


number = [5, 2, 5, 2, 2]
# iterates over every item in the list
for x_count in number:
    # sets output to an empty string
    output = ''
    # using the range to generate a sequence of numbers from 0 to x_count inner loop will execute 5x
    for count in range(x_count):
        # appends an x to each iteration of the output variable
        output += 'x'
    # this will print 5 xxxxx to the terminal. The returns to the first line for the second iteration.
    print(output)


numbers = [2, 2, 2, 2, 5]
# iterates over every item in the list
for X_count in numbers:
    # sets output to an empty string
    output = ''
    # using the range to generate a sequence of numbers from 0 to x_count inner loop will execute 2x
    for count in range(X_count):
        # appends an x to each iteration of the output variable
        output += 'x'
    # this will print 2 xx to the terminal. Then returns to the first line for the second iteration
    print(output)