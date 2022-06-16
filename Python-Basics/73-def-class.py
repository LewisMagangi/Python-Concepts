class Person:

    # constructor or initializer
    def __init__(self, name):
        self.name = name # name is data field also commonly known as instance variables

    # method which returns a string
    def whoami(self):
        return "You are " + self.name
