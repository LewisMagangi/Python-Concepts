'''
If the value associated with a key is a string, it is treated as a docstring and scanned for tests.
If the value is a class or function, doctest searches them recursively for docstrings, which are then scanned for tests.
In this example, the module doctest_private_tests_external has a single test in its docstring.
'''
# doctest_private_tests_external.py
"""External tests associated with doctest_private_tests.py.

>>> my_function(['A', 'B', 'C'], 2)
['A', 'B', 'C', 'A', 'B', 'C']
"""
