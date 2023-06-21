### our first function
def first_function():
    print("This is my first function ")


first_function()


### functions with parametres


def second_function(name):
    print("Hello" + name)


second_function("John")

### functions with multiple parameters

def third_function(name, age):
    print("Hello " + name + " you are " + str(age) + " years old")


third_function("John",36)


###functions with unkown parameters

def fourth_function(*names):
    print("The first name entered is " + names[1])
    print("The last name entered is " + names[-1])

fourth_function("John", "Mary", "Bob")


###Functions with keyword arguments

def fifth_function(name, age, gender):
    print("The name is " + name + " the age is " + age + " the gender is " +gender)


fifth_function(name="John", age="36", gender="Male")


### Functions with return values

def sixth_function(x):
    # passes the value to whatever is calling it
    return 10 * x

print(sixth_function(10))

number=sixth_function(10)
print(number)

#######

## create a function that accepts 2 parameters numbers and use these two numbers in a range method to print value

#######

def seventh_function(start, end):
    for number in range(start, end+1):
        print(number)


seventh_function(1, 50)

### keywords with unknown number of arguments
def eigth_function(**names):
    print("The first name entered is " + names["name1"])
    print("The last name entered is " + names["name2"])


eigth_function(name1="John", name2="Mary")


### variables scope

result = 3

def scope_test1():
    result = 42       ### global variable is not changed as it is local

scope_test1()
print(result)

def scope_test2():
    global result       ### global variable is changed as we have called global system object
    result = 42

scope_test2()
print(result)

### default parameter value

def ninth_function(country="Norway"):
    print("I am from " + country)

ninth_function()
ninth_function("UK")


# ### Passing a list as an argument
# fruits = ['apple', 'banana', 'cherry']
# def tenth_function(food):
#     for x in food:
#         print(x)
#
# tenth_function(fruits)

# def longest_fruit_name(fruits):
#     longest_name = ""
#     for fruit in fruits:
#         if len(fruit) > len(longest_name):
#             longest_name = fruit
#     return longest_name
#
#
# favorite_fruits = ["apple", "banana", "pineapple", "strawberry"]
# result = longest_fruit_name(favorite_fruits)
# print(result)  # Output: pineapple


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# number = int(input("Enter the number: "))
print(even_or_odd(number))


## factorial of n

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))









