# dictionary with key value pairs
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
# this is how we can add a new item to a dictionary
customer["birthdate"] = "Jan 1 1980"
# how to change an item in the dictionary without altering the original item
customer["name"] = "Jack Smith"
# how to access key value pairs
print(customer.get("name"))
# if something isn't in the dictionary then you can add a response following a comma
print(customer.get("birthdate", "Jan 1 1980"))
# how to change numbers to words using dictionaries
phone = input("Phone:")
my_dict = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}
# for item in phone:
#     if item in my_dict.keys():
#         phone = phone.replace(item, my_dict[item])
# print(phone)

# another way of achieving the same result but with a space between words and an ! for an un listed item
output = " "
for ch in phone:
    output += my_dict.get(ch, "!") + " "
print(output)



