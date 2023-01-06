def solution(num):
    i = 0
    l = 0
    while i < num:
        if i % 3 == 0 or i % 5 == 0 and i < num:
            l += i
        i += 1
        print(l)
    print(i)
solution(6)
