'''
Python program to demonstrate private members of the parent class
'''

class King(object):
    def __init__(self):
        self.publicvalue = 21

        '''privatevalue is private instance variable'''
        self.__privatevalue = 42

class Prince(King):
    def __init__(self):
        self.e = 84
        Prince.__init__(self)


object1 = King()

# produces an error as d is private instance variable
try:
    print(object1.privatevalue)
except AttributeError:
    print("The value is private")
