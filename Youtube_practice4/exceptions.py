# an example of an exception which stops an error message and replaces it with a message
# here we replace an error message which presents when no integer is entered by the user
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age can not be 0.')
except ValueError:
    print("Invalid value")

# 'try' 'except' are used for error handling

