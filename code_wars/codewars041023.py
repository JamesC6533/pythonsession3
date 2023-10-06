# string ends with
def solution(text, ending):
    return text.endswith(ending)


# opposite number
def opposite(number):
    return -number


# binary addition
def add_binary(a,b):
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
            diamond += " " * abs((n/2) - i)
            diamond += "" (n - abs((n-1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None


    def name_shuffler(s):
        return ' '.join(reversed(s.split()))


def validate_pin(pin):
    return pin.isdigit() and len(pin) == 4 or pin.isdigit() and len(pin) == 6


def pipe_fix(nums):
    pipes = nums
    for i in range(nums[0], nums[-1]+1):
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
    num_list = [int(num)for num in n.split()]
    return f'{max(num_list)} {min(num_list)}'


def other_angle(a,b):
    return 180 - a - b


def area_or_perimeter(l , w):
    return l * w if l == w else l * 2 + w * 2


def accum(s):
    return '-'.join([i.upper()+ i.lower() *(index)for index, i in enumerate(s)])


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


def grasshopper(l,c,ch):
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


