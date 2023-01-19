"""
Python program showing a use
of get() and set() method in
normal function
"""

class Lique:
    def __init__(self, age = 0):
        self._age = age

    # getter method
    def get_age(self):
        return self._age

    # setter method
    def set_age(self, x):
        self._age = x

raj = Lique()

print(raj._age)

# setting the age using setter
raj.set_age(18)

# retrieving age using getter
print(raj.get_age())

print(raj._age)
