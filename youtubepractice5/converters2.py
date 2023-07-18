from utils import find_max

print(max([10,3,4,5]))

print(max([10,45,63,22,105]))

# because max is a built in function we change the variable max to maximum
numbers = [10,45,63,22,105,334]
maximum = find_max(numbers)
print(maximum)