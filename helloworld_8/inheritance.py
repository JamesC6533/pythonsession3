class Animal:
    count = 0

    def __init__(self, species, name, sound):
        self._species = species
        self._name = name
        self._sound = sound
        Animal.count += 1

    @property
    def species(self):
        return self._species

    @classmethod
    def kill(cls):
        cls.count -= 1

    @property
    def name(self):
        return self._name

    def make_sound(self):
        print(self._sound)

    @classmethod
    def remove(cls):
        cls.count -= 1

    @classmethod
    def zoo_size(cls):
        return cls.count


# Creating instances of the Animal class
leo = Animal("African lion", "Leo", "Roarrrrr")
garfield = Animal("Cat", "Garfield", 'Meowwwww')
felix = Animal("Cat", "Felix", "Meowwwww")

# Accessing instance properties and calling methods
print(leo.name, "is a", leo.species)
leo.make_sound()
print(garfield.name, "is a", garfield.species)
garfield.make_sound()
print(felix.name, "is a", felix.species)
felix.make_sound()

# Printing the zoo size
print("Zoo size:", Animal.zoo_size())