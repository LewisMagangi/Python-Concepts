'''
All of the tests in the examples so far have been written in the docstrings of the functions they are testing.
That is convenient for users who examine the docstrings for help using the function (especially with pydoc), but doctest looks for tests in other places, too.
The obvious location for additional tests is in the docstrings elsewhere in the module.
'''

# doctest_docstrings.py
"""Tests can appear in any docstring within the module.

Module-level tests cross class and function boundaries.

>>> A('a') == B('b')
False
"""


class A:
    """Simple class.

    >>> A('instance_name').name
    'instance_name'
    """

    def __init__(self, name):
        self.name = name

    def method(self):
        """Returns an unusual value.

        >>> A('name').method()
        'eman'
        """
        return ''.join(reversed(self.name))

    
class B(A):
    """Another simple class.
    
    >>> B('different_name').name
    'different_name'
    """
