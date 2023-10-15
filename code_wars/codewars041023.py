# string ends with
def solution(text, ending):
    return text.endswith(ending)


# opposite number
def opposite(number):
    return -number


# binary addition
def add_binary(a, b):
    binary = bin(a + b)
    return str(binary)[2:]


# convert to boolean to string
def boolean_to_string(b):
    return str(b)


# removes vowls from a sting
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return "".join([i for i in string_ if i not in vowels])


# Convert a Number to a String!
def number_to_string(num):
    return str(num)


# bouncing balls
def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    count = 1
    while h * bounce > window:
        h = h * bounce
        count += 2
    return count


# beginner series clock
def past(h, m, s):
    hours = h * 3600
    minutes = m * 60

    return (hours + minutes + s) * 1000


# calculates the sum of people
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


def diamond(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n / 2) - i)
            diamond += ""(n - abs((n - 1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None

    def name_shuffler(s):
       return ' '.join(reversed(s.split()))


def validate_pin(pin):
    return pin.isdigit() and len(pin) == 4 or pin.isdigit() and len(pin) == 6


def validate_pin2(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()


def pipe_fix(nums):
    pipes = nums
    for i in range(nums[0], nums[-1] + 1):
        if i not in nums:
            pipes.append(i)

    return sorted(pipes)


def sale_hotdogs(n):
    return n * 100 if n < 5 else n * 95 if n < 10 else n * 90


def sale_hotdogs1(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)


def repeat_str(n, s):
    repeats = s * n

    return repeats


def repeat_str1(repeat, string):
    return repeat * string


# checks if item is an instance of specified item
def filter_list(l):
    return [i for i in l if isinstance(i, int)]


def is_pangram(s):
    return all(c in s.lower() for c in 'abcdefghijklmnopqrstuvwxyz')


def how_much_i_love_you(nb_petals):
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return phrases[(nb_petals - 1) % 6]


# returns the highest and lowest numbers in a list
def high_and_low(n):
    num_list = [int(num) for num in n.split()]
    return f'{max(num_list)} {min(num_list)}'


def other_angle(a, b):
    return 180 - a - b


def area_or_perimeter(l, w):
    return l * w if l == w else l * 2 + w * 2


def accum(s):
    return '-'.join([i.upper() + i.lower() * (index) for index, i in enumerate(s)])


def plural(n):
    return True if n != 1 else False


def reverse_list(l):
    l.reverse()
    return l


def reverse_list1(l):
    return l[::-1]


def increment_string(strng):
    letters = strng.rstrip('0123456789')
    digits = strng[len(letters):]
    if digits == "":
        return letters + '1'
    digits = str(int(digits) + 1).zfill(len(digits))
    return letters + digits


def grasshopper(l, c, ch):
    return l + c + ch


def abbrev_name(name):
    abbreviate = []
    names = name.split()

    for i in names:
        if i:
            abbreviate.append(i[0].upper())

    abbreviated = '.'.join(abbreviate)
    return abbreviated


def abbrevname(name):
    return '.'.join(i[0] for i in name.split()).upper()


def unique_in_order(iterable):
    result = []
    for i in iterable:
        i in result[-1:] or result.append(i)

    return result


def unique_in_order2(sequence):
    return [sequence[i] for i in range(len(sequence)) if not i or sequence[i] != sequence[i - 1]]


def unique_in_order3(sequence):
    unique_items = []

    for i in sequence:
        if not unique_items or i != unique_items[-1]:
            unique_items.append(i)

    return unique_items


def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s


def get_middle2(s):
    # checks if the word has odd or even no. of letters
    if len(s) % 2 == 0:
        # if word has even no. of letters then return 2 middle letters
        return s[len(s)//2 - 1] + s[len(s)//2]
    else:
        # if not then return center letter
        return s[(len(s) - 1)//2]


def get_middle3(s):
    return s[len(s)//2] if len(s) % 2 != 0 else s[len(s)//2-1:len(s)//2+1]


def solution1(n):

    if n % 10 == 0:
        return n + 10
    else:
         return (n// 10 + 1)*10


def solutions(S):
    # Create a dictionary to map words to their corresponding values
    word_to_value = {"one": 1, "two": 2}

    # Initialize the result to the first word's value
    result = word_to_value[S.split("+")[0]]

    # Split the string by the '+' and '-' signs
    segments = S.split('+')

    for segment in segments[1:]:
        if '-' in segment:
            parts = segment.split('-')
            for part in parts:
                if part == 'one':
                    result -= 1
                elif part == 'two':
                    result -= 2
        else:
            if segment == 'one':
                result += 1
            elif segment == 'two':
                result += 2


def solution2(S):
    diction = {"one": 1, "two": 2, "+": 0, "-": 0}

    char = S.replace("+", " + ")
    chars = char.replace("-", " - ")
    number = chars.split()

    result = 0

    current_op = 1

    for i in number:
        if i in ("+", "-"):
            current_op = 1 if i == "+" else -1
        else:
            result += current_op * diction.get(i , 0)
    return result


def printer_error(s):
    # Define the range of valid colors (a to m)
    valid_colors = set("abcdefghijklm")

    # Count the number of characters in the string that are not in the valid colors
    error_count = sum(1 for char in s if char not in valid_colors)

    # Calculate the error rate as a string in the requested format
    error_rate = f"{error_count}/{len(s)}"

    return error_rate


def printer_errors(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m":
            errors += 1
    return str(errors) + "/" + str(count)


def printer_error1(s):
    good_colors = "abcdefghijklm"
    counter = 0
    for i in s:
        if i not in good_colors:
            counter += 1
    return str(counter) + "/" + str(len(s))


def find_needle(haystack):
    index = haystack.index("needle")
    return f"found the needle at position {index}"


def find_needles(haystack):
    position = 0
    for range in haystack:
        if (range == 'needle'):
            return 'found the needle at position %s' % (position)
        else:
            position += 1


def check(seq, elem):
    return True if elem in seq else False


def checks(seq, elem):
    return elem in seq


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


def smash(words):
    return " ".join(words)


def is_isogram(string):
    string = string.lower()

    seen = set()

    for i in string:
        if i.isalpha():
            if i in seen:
                return False

        seen.add(i)

    return True


def is_isograms(string):
    return len(string) == len(set(string.lower()))


def is_isogram1(string):
    s = set(string.lower())
    if len(s) == len(string):
        return True
    return False


def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)

    lowest_numbers = sorted_numbers[:2]

    return sum(lowest_numbers)


def sum_two_smallest_numbers1(numbers):
    return sum(sorted(numbers)[:2])


def better_than_average(class_points, your_points):
    class_average = (sum(class_points) + your_points) / (len(class_points) + 1)
    return your_points > class_average


def better_than_average1(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)


import math


def find_next_square(sq):
    if math.isqrt(sq)**2 == sq:
        next_sq = (math.isqrt(sq) + 1) ** 2
        return next_sq
    else:
        return -1


def find_next_squared(sq):
    sqrt=sq**(0.5)
    if sqrt % 1 == 0:
        return (sqrt+1)**2
    return -1


def get_count(sentence):
    vowels = set("aeiou")

    count = 0

    for i in sentence:
        if i in vowels:
            count += 1

    return count


def get_count1(sentence):
    return sum(i in 'aeiou' for i in sentence)


def count_by(x, n):
    multiples = [x * i for i in range(1, n + 1)]
    return multiples


def count_by1(x, n):
    arr = []
    for num in range(1, n+1):
        result = x * num
        arr.append(result)
    return arr


def dna_to_rna(dna):
    rna = dna.replace('T', 'U')
    return rna


def dna_to_rna1(dna):
    return dna.replace("T", "U")


def odd_or_even1(arr):
    n = sum(arr)
    return "odd" if n % 2 != 0 else "even"


def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


def solutionb(string):
    reversed_string = string[::-1]

    return reversed_string


def solutionz(string):
    return ''.join(i for i in reversed(string))


def open_or_senior(data):
    return ["Senior" if i[0] >= 55 and i [1] > 7 else "Open" for i in data]


def open_or_senior1(data):
    res = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        res.append("Senior")
      else:
        res.append("Open")
    return res


def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"


def alphabet_position(text):
    res = []

    for i in text:
        if i.isalpha():
            i = i.lower()
            position = ord(i) - ord('a') + 1
            res.append(str(position))
    return ' '.join(res)



def alphabet_position1(s):
  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())

