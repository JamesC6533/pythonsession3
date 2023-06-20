# define a meaningful function name
# gives the square of a number, pass number to the parameter
def square(number):
    # multiply value by value
    return (number * number)

# argument for the print function which gives the return a value to use
print(square(3))


def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😞",
        ">:(": "😡"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))












