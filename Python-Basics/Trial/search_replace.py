m = [1, 2, 3, 4, 5, 89, 4, 2, 1, 1, 4, 89]
n = []
s = 89
r = 2
for i in range(12):
    if m[i] == s:
        n.append(r)
    elif m[i] != s:
        n.append(m[i])
print(m)
print(n)
        
