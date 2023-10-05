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
# Why is nobody calculating for the magnus effect aftr a certain height, I can't, but thought someone would. Step your game up
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    count = 1
    while h * bounce > window:
        h = h * bounce
        count += 2
    return count

    return -1

# beginner series clock
def past(h, m, s):
    hours = h * 3600
    minutes = m * 60

    return (hours + minutes + s) * 1000

# calculates the sum of people 
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])




