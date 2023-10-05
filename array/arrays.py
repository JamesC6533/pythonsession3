# def solution(A):
#     n = len(A)
#     count = 0
#     for i in range(0,n-1):
#         if A[i] == A[i+1]:
#             count += 1
#             if A[i] == 0:
#                A[i+1] = 1
#             else:
#                 A[i+1] = 0
#
#     return count
#
# A = [1,0,1,1,0]
# print(solution(A))

def valid_string(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


def gimme_the_letters(sp):
    start, end = sp.split('-')
    return ''.join([chr(i) for i in range(ord(start), ord(end) + 1)])


def get_characters(character_range):
    start, end = character_range.split('-')
    characters = []

    start_num = ord(start)
    end_num = ord(end)

    for num in range(start_num, end_num + 1):
        character = chr(num)
        characters.append(character)

    result = ''.join(characters)
    return result


def make_negative( number ):
    return -abs(number)


def likes(names):
    # Check the number of people who liked the item.
    num_likes = len(names)

    if num_likes == 0:
        return "no one likes this"
    elif num_likes == 1:
        return f"{names[0]} likes this"
    elif num_likes == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num_likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        others = num_likes - 2
        return f"{names[0]}, {names[1]} and {others} others like this"


    # This calculates how many juice the rider has consumed at a rate of 0.5 litres an hour

    def litres(time):
        return int(time * 0.5)

    # change operator to string from maths symbol

    def arithmatic(a,b,operator):
        return {
            'add': a + b,
            'subtract': a - b,
            'multiply': a * b,
            'divide': a / b,
        }[operator]




    def twice_as_old(dad_years_old, son_years_old):
     age_difference = dad_years_old - son_years_old

        if age_difference == son_years_old:
        return 0
        else:
        years_ago = abs(age_difference - son_years_old)
        return years_ago




from functools import reduce
from operator import mul
def get_digits(number):
    """Generates digits of a number."""
    while number:
        digit = number % 10
        yield digit
        # remove last digit from number (as integer)
        number //= 10
def persistence(number, count=0):
    if number < 10:
        return count
    # get new number by multiplying digits of a number
    new_number = reduce(mul, get_digits(number))
    return persistence(new_number, count + 1)

# multiplication persitence, keeps multiplying until the sum of the last result is a single digit
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count

# create a function that
def unusual_five():
    return len("five!")



def high_and_low(numbers):
    num_list = [int(num) for num in numbers.split()]
    return f"{max(num_list)} {min(num_list)}"









