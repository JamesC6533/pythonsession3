class Animal:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
     print("The animal makes a sound")


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("This dog barks")


# creating instances of classes
animal = Animal("Generic Animal Name")
dog = Dog('Dog', 'Labrador')

animal.make_sound()
dog.make_sound()
