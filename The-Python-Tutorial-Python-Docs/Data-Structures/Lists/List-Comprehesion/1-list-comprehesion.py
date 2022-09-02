"""
List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

For example, assume we want to create a list of squares, like:
"""

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

triples = list(map(lambda x: x**3, range(10)))
print(triples)

doubles = []
doubles = [x + x for x in range(10)]
print(doubles)
