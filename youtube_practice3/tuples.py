# tuples are defined by () parenthesis. tuples are immutable. you can only get info from a tuple
numbers = (1, 2, 3)
# returns the first item from the tuple
print(numbers[0])

# UNPACKING
coordinates = (1, 2, 3)
# two ways to store the values of the tuple and store them in variables
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
# takes the first item in the tuple and assigns it to the first variable, 2nd to the 2nd and 3rd to the 3rd
x, y, z = coordinates
print(z)
# this can also be done with list just using [] to define the list
