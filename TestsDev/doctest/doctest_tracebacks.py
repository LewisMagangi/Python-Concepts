"""
Tracebacks are a special case of changing data.
Since the paths in a traceback depend on the location where a module is installed on the file system,
it would be impossible to write portable tests if they were treated the same as other output.
doctest makes a special effort to recognize tracebacks, and ignore the parts that might change from system to system.
"""

# doctest_tracebacks.py
def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/no/such/path/doctest_tracebacks.py", line 14, in
      this_raises
        raise RuntimeError('here is the error')
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')
