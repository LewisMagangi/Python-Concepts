#Illustration of the enumerate function
fruits = ['apples', 'banana', 'cherries']

for i, fruit in enumerate(fruits, start=0):
    print("Index {} : {}".format(i, fruit))
