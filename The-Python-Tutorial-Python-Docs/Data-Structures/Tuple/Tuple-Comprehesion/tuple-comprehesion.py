"""
If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized for comprehesion syntax.
"""

print([(x, x**2) for x in range(6)])
print([(x, x**3) for x in range(6)])
