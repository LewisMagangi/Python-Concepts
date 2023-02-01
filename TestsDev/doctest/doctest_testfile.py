'''
testfile() works in a way similar to testmod(), allowing the tests to be invoked explicitly in an external file from within the test program.
'''
# doctest_testfile.py
import doctest

if __name__ == '__main__':
    doctest.testfile('doctest_in_help.txt')
