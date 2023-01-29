"""
doctest also allows for surrounding text.
It looks for lines beginning with the interpreter prompt (>>>) to find the beginning of a test case,
and the case is ended by a blank line or by the next interpreter prompt. 
Intervening text is ignored, and can have any format as long as it does not look like a test case.
"""
def my_function(a, b):
    """
    Returns a * b.

    Works with numbers:

    >>> my_function(2, 3)
    6

    and strings:

    >>> my_function('a', 3)
    'aaa'
    """
    return a * b
