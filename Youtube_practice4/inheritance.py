class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Bark!")


class Cat(Mammal):
    def be_amazing(self):
        print("Has wares if you has coin!")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_amazing()
