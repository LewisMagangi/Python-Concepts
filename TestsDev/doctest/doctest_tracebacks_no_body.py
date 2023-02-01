'''
In fact, the entire body of the traceback is ignored and can be omitted.
When doctest sees a traceback header line (either “Traceback (most recent call last):” or “Traceback (innermost last):”,
to support different versions of Python), it skips ahead to find the exception type and message, ignoring the intervening lines entirely.
'''
# doctest_tracebacks_no_body.py
def this_raises():
    """This function always raises an exception.
        
    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: here is the error

    >>> this_raises()
    Traceback (innermost last):
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')
