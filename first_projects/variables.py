first_name = "James"
print (first_name)

last_name = "Cotterill"
print(last_name)
number1 = 11
number2 = 17
# * is a multiply operator
answer = number1 * number2
print(answer)
zak_number = 13
# / is a divide operator
answer2 = answer / zak_number
print(answer2)
print(round(answer2, 2))
# print(round(answer2, 2)) # use the round function to round to the number 2 decimal places
if number1 > zak_number:
    print("number one is higher than zak's number")
elif number1 == zak_number:
    print("number 1 is = zak's number")
else:
    print("number 1 is less than zak's number")


fullname = first_name + last_name
print(fullname)

fullname_with_space = first_name + ' ' + last_name
print(fullname_with_space)

answer3 = number1 + number2
print(answer3)

print(type(first_name))

print(type(number1))

print(type(answer2))

print(first_name)
print(first_name.upper()) # this is a METHOD
# methods belong to OBJECTS
print(first_name)