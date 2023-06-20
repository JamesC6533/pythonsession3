numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)
# insert an item to the list
numbers.insert(0,10)
print(numbers)
# removes an item from the list
numbers.remove(20)
print(numbers)
# clears the items from the list
# numbers.clear()
# print(numbers)
# removes an item from the end of the list
numbers.pop()
print(numbers)
# returns the index of the first occurrence of the item in the list. It will tell you if a value isnt listed
print(numbers.index(5))
# checks the existence of an item in a list and return a boolean value
print(50 in numbers)
# count the number of times an item occurs in a list
print(numbers.count(5))
# this sorts the list into an ascending order
numbers.sort()
print(numbers)
# this sorts the list into a descending order
numbers.reverse()
print(numbers)
# this is to copy a list the original list can then be edited, but it wont change the copied list
number2 = numbers.copy()
print(number2)
# this is how to remove duplicates from lists
numbers1 = [5, 3, 3, 5, 7, 8, 9]
uniques = []
for number in numbers1:
    if number not in uniques:
        uniques.append(number)
print(uniques)

