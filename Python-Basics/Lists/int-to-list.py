"""
Convert the integer to string first, and then use map to apply int on it:
"""
num = 132985355
print(list(map(int, str(num))))

"""
using a list comprehension:
"""
x =  [int(x) for x in str(num)]
print(x)
