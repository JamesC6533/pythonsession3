from electrical import *
from navigation import *

print(current())
print(voltage())
print(amps())

# main

import sys


# other imports (standard library, standard non-library, local)

# constants (AKA global variables)

# main function
def main(args):
    function1()
    function2()


#other functions
def function1():
    print("hello from function1()")


def function2():
    print("hello from function2()")


if __name__ == "__main__":
    main(sys.argv[1:])

