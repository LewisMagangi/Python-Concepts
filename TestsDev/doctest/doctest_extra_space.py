'''
Whitespace within a line can also cause tricky problems with tests. This example has a single extra space after the 6.
Extra spaces can find their way into code via copy-and-paste errors, but since they come at the end of the line,
 they can go unnoticed in the source file and be invisible in the test failure report as well.
'''
def my_function(l, b):
    """
    >>> my_function(2, 3)
    6         
    >>> my_function('a', 3)
    'aaa'
    """
    return l * b
