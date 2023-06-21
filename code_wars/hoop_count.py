def hoop_count(n):
    if n >= 10:
        return "Great, now move onto tricks "
    else:
        return "Keep at it until you get it!"


Hoops = int(input("Hoop count: "))
print(hoop_count(Hoops))