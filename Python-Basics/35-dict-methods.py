friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}
print("Before using .popitem")
print(friends)
friends.popitem()
print("After")
print(friends)

print("Before  using .clear")
print(friends)
friends.clear()
print("After")
print(friends)

friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}
print("Accessing keys using .keys")
print(friends.keys())

print("Accessing dictionary values using .values")
print(friends.values())

print("Accessing the value of tom using .get")
print(friends.get('tom'))

print("Before removing an item from a dictionary using .pop")
print(friends)
friends.pop('bob')
print("After")
print(friends)
