'''
A Python program to demonstrate inheritance

Base or Super class. Note object in bracket.
(Generally, object is made ancestor of all classes)
In Python 3.x "class Person" is
equivalent to "class Person(object)"
'''

class Parent(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Parent):

    # Constructor
    def __init__(self, name, age):
        Parent.__init__(self, name)
        self.age = age

    # To get name
    def getAge(self):
        return self.age
    
# Inherited or Sub class (Note Person in bracket)

class GrandChild(Child):

    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
                            
    # To get address
    def getAddress(self):
        return self.address
    
    
# Driver code
g = GrandChild("LOISE", 23, "Utawala")
print(g.getName(), g.getAge(), g.getAddress())
