# # emojis in python
# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😀",
#     ":(": "😞",
#     ">:(": "😡"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# functions, use meaningful descriptions for functions
# def greet_user():
#     print("Hi there!")
#     print("Welcome aboard!")
#
# # start of the code
# print("Start")
# # function is called so jumps to the greet_user block
# greet_user()
# # jumps back down here to finish the code
# print("Finish")

# parameters
# add parameters to pass a value to a function
# in this example the parameter passes the with formatted strings f {} to the print statement
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard!")

# start of the code
print("Start")
# function is called so jumps to the greet_user block
greet_user("John", "Smith")
# call the function again with another value 
greet_user("Amber", "MacDonald")
# jumps back down here to finish the code
print("Finish")

# keyword argument examples, good for labelling values so others can read and understand
greet_user(last_name="Smith", first_name="John")
calc_cost(total=50, shipping=5, discount=0.1)

