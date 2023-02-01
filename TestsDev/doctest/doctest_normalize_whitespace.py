'''
There are cases where it is beneficial to add extra whitespace in the sample output for the test, and have doctest ignore it.
For example, data structures can be easier to read when spread across several lines, even if their representation would fit on a single line.
'''
def my_function(n, b):
    """Returns n * b.

    >>> my_function(['A', 'B'], 3) #doctest: +NORMALIZE_WHITESPACE
    ['A', 'B',
     'A', 'B',
     'A', 'B']
    """
    return n * b
