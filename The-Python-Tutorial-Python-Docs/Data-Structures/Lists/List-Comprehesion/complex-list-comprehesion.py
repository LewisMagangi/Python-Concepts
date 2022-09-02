"""
List comprehensions can contain complex expressions and nested functions:
"""

from math import pi
print([str(round(pi, i)) for i in range(1, 8)])
