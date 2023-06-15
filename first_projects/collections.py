person1 = "Jay"
person2 = "Adam"
person3 = "Adrian"

# tuple
person_tuple = "Jay", "Adam", "Adrian"

print(person_tuple)
print(type(person_tuple))

person_tuple2 = ("James", "Chris", "Elson")

print(person_tuple2)
print(type(person_tuple2))

numbers_tuple = 26, 5, 22
print(numbers_tuple)
print(type(numbers_tuple))

# lists
# Lists are called arrays in other languages
person_list = ["Matt", "Pat", "Chris"]
print(person_list)
print(type(person_list))

# tuples are IMMUTABLE
# lists are MUTABLE

person_list.append("Pete")
print(person_list)

# print me thr name at position 1
print(person_list[1])
print(person_list[3])
print(person_list[2])
print(person_list[0])
# coders count from ZERO

print(person_tuple[0])
person_list [0] = "Zippy"
print(person_list)
# person_tuple[0] = "George" # i have commented out the modification to the tuple as they are IMMUTABLE

# dictionaries
# key value pairs

hobbies_dictionary = {"Bart": "Skateboarding", "Lisa": "Playing sax", "Maggie": "Dummy"}