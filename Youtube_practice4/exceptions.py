# an example of an exception which stops an error message and replaces it with a message
# here we replace an error message which presents when no integer is entered by the user
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("Invalid value")
