import gc


# base class declared
class AnimalBase():
    def __init__(self, name):
        self._name = name

    def get_id(self):
        print(self._name)


# mixin classes are declared mixin and baseclass as parameters 
class CanBark():
    def bark(self):
        print("Woof - Woof!")


class CanFly():
    def fly(self):
        print("I'm flying!")

class Dog(CanBark, AnimalBase):
    pass

class Sparrow(CanFly, AnimalBase):
    pass


d = Dog('Dennis')
d.get_id()
d.bark()
print()

s = Sparrow('Steve')
s.get_id()
s.fly()
print()

print("Sparrow mro:", Sparrow.mro())
print()
print("Dog mro:", Dog.mro())