def fun_one():
    print("Hello, world")


print("fun_one():", end=' ')
fun_one()
print()


# will return the parameter squared
def fun_two(n):
    return n ** 2


x = fun_two(5)
print("fun_two(5) is {}\n".format(x))


def fun_three(count=3):
    for _ in range(count):
        print("spam", end=' ')
        print()


fun_three()


fun_three(10)
print()


# positional argument of n, optional arguments are anything after *
def fun_four(n, * opt):
    print("fun_four():")
    print("n is", n)
    print("opt is", opt)
    # this prints symbols that are within the ' ' times by the number entered
    print('-' * 20)
    print()


fun_four('apple', 'banana', 'blueberry', 'cherry')


def fun_five(*, spam=0, eggs=0):
    print("fun_five():")
    print("spam is", spam)
    print("eggs is", eggs)
    print()


fun_five(spam=1, eggs=2)

fun_five(eggs=2, spam=1)
# in this example no value for eggs is called, but will still print 0 as its set as 0 in the def
fun_five(spam=1)

fun_five(eggs=1)
# in this example no parameters are passed so the default values set in the def print
fun_five()


# in this example we set named parameters and call them in the function
def fun_six(**named_args):
    print("fun_six():")
    for name in named_args:
        print(name, "==> ", named_args[name])


# any named parameters entered here will print in the terminal
# these are passed to the function as a dictionary with the key value pairs
fun_six(name="lancelot", quest="grail", colour="red")


# two positional parameters, one is set with a default parameter
def spam(greeting, whom='world'):
    print("{}, {}".format(greeting, whom))


# call function
spam("Hello")
spam("Hello","Mum")
print()


def ham(*, file_name, file_format='txt'):
    print("Processing {} as {}".format(file_name, file_format))


ham(file_name='eggs')
ham(file_name='toast', file_format='csv')

# global scoped variable
x = 42


def function_a():
    # local scope variable
    y = 5

    def function_b():
        # nested local scope variable
        z = 32
        print("function_b(): z is", z)
        print("function_b(): y is", y)
        print("function_b(): x is", x)
        print("function_b(): type(x) is", type(x))
    return function_b()

f = function_a()














