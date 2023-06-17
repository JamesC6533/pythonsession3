#  in this example the user enters a weight, if it is in lbs it will convert to kg and vice versa

#
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
