#named indexes:
t1 = "My name is {firstname}, I'm {age}".format(firstname = "Lewis", age = 16)

#numbered indexes:
t2 = "My name is {0}, I'm {1}".format("Mike",56)

#empty placeholders:
t3 = "My name is {}, I'm {}".format("John",36)

print(t1)
print(t2)
print(t3)
