# Python program to illustrate
# enumerate function
list1 = ["eat", "sleep", "code", "repeat"]
string1 = "geekforgeeks"

# creating enumerate objects
obj1 = enumerate(list1)
obj2 = enumerate(string1)

print ("Return type:", type(obj1))
print (list(enumerate(list1)))

# changing start index to 5 from 0
print (list(enumerate(string1, 5)))
