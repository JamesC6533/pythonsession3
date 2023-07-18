# when naming classes we capitalise the first letter
# of each word and each word is conjoined
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# to create an object we type out the name of a class and call it like a function.
point = Point(10,20)
point.x = 11
print(point.x)







class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person = Person("John Smith")
person.talk()

bob = Person("Bob Smith")
bob.talk()

