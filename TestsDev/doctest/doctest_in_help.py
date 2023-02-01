'''
Mixing tests in with regular code is not the only way to use doctest.
Examples embedded in external project documentation files, such as reStructuredText files, can be used as well.
'''
# doctest_in_help.py
def my_function(a, b):
    """Returns a*b
    """
    return a * b
