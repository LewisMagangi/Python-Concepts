# keys for the dictionary
alphabets = ['a', 'b', 'c']

print(alphabets)
# creates a dictionary from the list
dictionary = dict.fromkeys(alphabets, 1)

print(dictionary)

# Output: {'a': 1, 'c': 1, 'b': 1}
