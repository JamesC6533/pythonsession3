def hello_world(S=""):
    return "Hello" + S

print(hello_world())
print(hello_world("World"))

def add (x, y):
    return x+y, x-y

print(add(5,3))

add_result, subtract_result = add (5,3)
print(add_result)
print(subtract_result)

def reassign(number01):
    number01 = 2

number02 = 1
reassign(number02)
print(number02)

def reassign(number01):
    number01 = 2
    number01

number02 = 1
reassign(number02)
print(number02)

def reassign(number01):
    number01 = 2
    print(number01)

print(reassign(number02))
print(number02)

def reassign(list01):
    list01 = [2,3]
    print(list01)

def append(list02):
    list02.append(4)
    print(list02)

list03 = [0, 1]
reassign(list03)
append(list03)

