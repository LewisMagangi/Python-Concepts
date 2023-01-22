mx = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

t = [i for i in mx]

n = lambda m: m * m
for i in range(len(t)):
    for x in range(len(t[i])):
        t[i][x] = n(t[i][x])
        print(t[x])
print(t)
print(mx)
