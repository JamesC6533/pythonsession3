# when naming classes we capitalise the first letter
# of each word and each word is conjoined
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

# to create an object we type out the name of a class and call it like a function.
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)




