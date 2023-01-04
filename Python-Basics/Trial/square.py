num = 132
num = (list(map(int, str(num))))    #note, This will return a map object in pytho
newlist = [i * i for i in num]
print([int(i) for i in newlist])
