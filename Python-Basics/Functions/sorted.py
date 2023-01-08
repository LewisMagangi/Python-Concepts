"""
Syntax: sorted(iterable, key, reverse)

Parameters: sorted takes three parameters from which two are optional. 

Iterable: sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted.
Key(optional): A function that would serve as a key or a basis of sort comparison.
Reverse(optional): If True, then the iterable would be sorted in reverse (descending) order, by default it is set as False.
Return: Returns a list with elements in sorted order.
"""
# List
x = ['q', 'w', 'r', 'e', 't', 'y']
print(sorted(x))

# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print(sorted(x))

# String-sorted based on ASCII translations
x = "python"
print(sorted(x))

# Dictionary
x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
print(sorted(x))

# Set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print(sorted(x))

# Frozen Set
x = frozenset(('q', 'w', 'e', 'r', 't', 'y'))
print(sorted(x))
