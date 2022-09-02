friends = {
    'tom' : '111-222-333',
    'jerry' : '666-33-111'
    }
friends['bob'] = '888-999-666'
print("Before deleting")
print(friends)

del friends['tom']
print("After deleting")
print(friends)

print("Length of the dictionary is")
print(len(friends))

print("Is bob my friend ?")
print('bob' in friends)

print("Is jerry my enemy ?")
print('jerry' not in friends)
