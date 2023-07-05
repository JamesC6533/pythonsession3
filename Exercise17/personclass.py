class Person:
    # Keeps track of the number of instances starts at 0
    count = 0

    # Constructor initialises with parameters given
    def __init__(self, nationality, name, language):
        # Instance variables that store vales passed to the constructor
        self._nationality = nationality
        self._name = name
        self._language = language
        # Increments the count by 1 every time a new instance is created
        Person.count += 1

    # Decorator allows access to nationality, provides getter method for self nationality
    @property
    def nationality(self):
        return self._nationality

    # Decorator that makes the kill method a class method
    # The kill method decreases the count by 1 when called, operates on cls rather than instance
    @classmethod
    def kill(cls):
        cls.count -= 1

    # Decorator allows access to name, provides a getter method for self name
    @property
    def name(self):
        return self._name

    # Prints the value self language
    def what_language(self):
        print(self._language)

    # Decorator makes the remove method a class method,
    # Remove method decreases the count by 1 when called
    # Operates on the class cls rather than an instance
    @classmethod
    def remove(cls):
        cls.count -= 1

    # Decorator makes the head_count method a class method,
    # The head_count method returns the current value of count
    @classmethod
    def head_count(cls):
        return cls.count


# Creating instances of the Person class
James = Person("England", "James", "Hello!")
Rene = Person("France", "Rene", 'Bonjour!')
Juan = Person("Spain", "Juan", "Hola!")

# Accessing instance properties and calling methods
print(James.name, "is from", James.nationality)
James.what_language()
print(Rene.name, "is from", Rene.nationality)
Rene.what_language()
print(Juan.name, "is from", Juan.nationality)
Juan.what_language()

# Printing the head count
print("Head count:", Person.head_count())