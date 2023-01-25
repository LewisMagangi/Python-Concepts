def hi(obj):
    print("Naitwa " + obj.name + "!")
"""
We will now bind the function „hi“ to a class attribute „say_hi“!
"""
class Robot:
    say_hi = hi
x = Robot()
x.name = "Marvo"
Robot.say_hi(x)
