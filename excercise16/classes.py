class Person:
    name = ""
    age = 0
    height = 0
    weight = 0
    nationality = ""
    hobbies = []

    def __init__(self, name, age, height, weight, nationality):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.nationality = nationality
        self.hobbies = []

    def height_gain(self, height):
        self.height += height
        # rounds number to one decimal place, by multiplying self.height by 10
        # then convert to an integer, and then divide it by 10.
        self.height = int(self.height * 10) / 10
        return self.height

    def height_loss(self, height):
        self.height -= height
        self.height = int(self.height * 10) / 10
        return self.height

    def another_birthday(self,age):
        self.age += age
        return self.age

    def gained_a_few(self, weight):
        self.weight += weight
        return self.weight

    def lost_a_few(self, weight):
        self.weight -= weight
        return self.weight

    def interests(self, hobbies):
        self.hobbies += hobbies
        return self.hobbies

    def remove_interest(self, hobby):
        if hobby in self.hobbies:
            self.hobbies.remove(hobby)
        else:
            print(f"{hobby} is not in the hobbies list.")

    def person_info(self):
        return self.name, self.age, self.height, self.weight, self.nationality, self.hobbies


person = Person("Ian", 48, 6.1, 120, "British")
print(person.name)
print(person.age)
print(person.height)
print(person.weight)
print(person.nationality)

person.height_gain(0.5)
print(person.height)

person.height_loss(0.5)
print(person.height)

person.another_birthday(10)
print(person.age)

person.gained_a_few(100)
print(person.weight)

person.lost_a_few(110)
print(person.weight)

person.interests(["Football", "Cooking", "Films", "Socialising", "Gardening", "Ballet"])
print(person.hobbies)

person.remove_interest("Ballet")
print(person.hobbies)

person.person_info()
print("Personal info:",person.person_info())


