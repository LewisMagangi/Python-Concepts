x = 0
mult = 1
n = 999
n = list(map(int, str(n)))

while len(n) > 1:
    for i in range(len(n)):
        mult *= n[i]
    n = list(map(int, str(mult)))
    mult = 1
    print(n)
    print(x)
    x += 1
