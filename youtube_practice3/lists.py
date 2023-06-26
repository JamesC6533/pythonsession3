names =['John', 'Bob', 'James', 'Mosh', 'Amber']
# this will alter list items in a list
names[0] = 'Jon'
# returns a specific index from a list, it also creates a new list so the original list is unaltered
print(names[2:])
print(names)

numbers = [2, 5, 8, 14, 35, 45]
# returns the largest (max) or smallest number (min)
print(min(numbers))
print(max(numbers))

Number = [2, 5, 45, 14, 35, 8]
max = Number[0]
for number in Number:
    if number > max:
        max = number
        print(max)

# 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# modifies items in the list
matrix[0][1] = 20
# how to select an item from the matrix list using 2 square brackets first bracket returns the inner list
print(matrix[0][1])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# iterates over the matrix list, each iteration will have one row
for row in matrix:
    for item in row:
        # prints all list items as a row
        print(item)

# remove every other item from a list
def remove_every_other(mylist):
    return mylist[::2]



# slicing examples 
def remove_every_other(my_list):
    return (my_list[::-1])


print(remove_every_other(["one", "two", "three", "four"]))