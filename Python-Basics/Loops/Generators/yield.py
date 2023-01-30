def reverse(string):
    for index in range(len(string)-1, -1, -1):
        yield string[index]

for char in reverse('swimming'):
    print(char)
            
