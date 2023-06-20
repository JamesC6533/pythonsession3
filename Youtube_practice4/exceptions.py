# an example of an exception which stops an error message and replaces it with a message
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("Invalid value")
