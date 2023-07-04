class Spam():

    def eggs(self):
        pass

    def _beverage(self):
        pass


s = Spam()

s.eggs()

s.toast = 'buttered'

print(s.toast)


class Rabbit:

    def __init__(self, size, danger):
        self._size = size
        self._danger = danger
        self._victims = []

    def threaten(self):
        print("I am a {} bunny with {}!".format(self._size, self._danger))


r1 = Rabbit('large', 'sharp pointy teeth')
r1.threaten()

r2 = Rabbit('small', 'fluffy and furry')
r2.threaten()


class Knight(object):
    def __init__(self, name):
        self._name = name

    # setter for the attribute
    def set_name(self, name):
        self._name = name

    # getter for the attribute
    def get_name(self):
        return self._name


k = Knight('Lancelot')
print(k.get_name())

k.set_name('James')

print(k.get_name())


class Knight(object):
    def __init__(self, name, title, color):
        self._name = name
        self._title = title
        self.color = color

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def title(self):
        return self._title


k = Knight('Lancelot', 'Sir', 'blue')

print('The knights name was {}-{} his favorite colour is {}'.format(k.title, k.name, k.color))

k.color = 'red'

print('The knights name was {}-{} his favorite colour is {}'.format(k.title, k.name, k.color))


class Rabbit:
    LOCATION = "the Cave of Caerbannog"

    def __init__(self, weapon):
        self.weapon = weapon

    def display(self):
        print("This rabbit guarding {} uses {} as a weapon".format(self.LOCATION, self.weapon))


r1 = Rabbit('a nice cup of tea')

r1.display()

r1 =Rabbit('big pointy teeth')

r1.display()


class Rabbit:
    LOCATION = "the Cave of Caerbannog"

    def __init__(self, weapon):
        self.weapon = weapon

    def display(self):
        print("This rabbit guarding {} uses {} as a weapon".format(self.LOCATION, self.weapon))

    @classmethod
    def get_location(cls):
        return cls.LOCATION


r = Rabbit('a nice cup of tea')
print(Rabbit.get_location())
print(r.get_location())