class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Define a "name" getter
    @property
    def name(self):
        return self._name

    # define a "name" deleter
    @name.deleter
    def name(self):
        del self._name
    
# Create a new Person object
person = Person("Alice", 30)

# access, set, and delete the "name" attribute
# using the getter, setter, and deleter
print(person.name)  # "Alice"

del person.name
try:
    print(person.name)  # AttributeError
except AttributeError:
    print("Name not found it's probably deleted")
