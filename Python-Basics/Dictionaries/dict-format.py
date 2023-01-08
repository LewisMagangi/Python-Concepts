"""
Syntax:

"{key}".format(**dict)
"""
dict1 = {"Python":"ABCD","Java":"BII","Cpp":"DEEP"}
res = "{Python} {Java}".format(**dict1)
print(res)
