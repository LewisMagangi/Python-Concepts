class Person:
        def __init__(self, name, age):
            self._name = name
            self._age = age
            
        # Define a "name" getter
        @property
        def name(self):
            return self._name
        
        # Define a "name" setter
        @name.setter
        def name(self, value):
            self._name = value
            
# Create a new Person object
person = Person("Alice", 30)

# Access and set the "name" attribute using the getter and setter
print(person.name)  # "Alice"

person.name = "Bob"
print(person.name)  # "Bob"
