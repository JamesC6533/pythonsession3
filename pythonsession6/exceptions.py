# catch errors without specifying the name
try:
    print(name)
except:
    print("an error has occurred")



# catch a NameError

try:
    print(name)
except NameError:
    print("Your variable has not been defined")
except:
    print("Some other error occurred")


#
filename = ()
error = ""

try:
    f=open(filename)
except FileNotFoundError:
    error = filename + "not found"
except (ValueError, TypeError):
    error = "Invalid filename"
except:
    print("Some other error occurred")
else:
    print("No error occurred")
finally:
    print("Finally block was run")

print(error)