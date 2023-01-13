tuple_a = ()
tuple_b = ()
#print(int(tuple_a[1]) + int(tuple_a[3]))
 
ta = list(tuple_a)
tb = list(tuple_b)
list_t = [0, 0]

if len(ta) == 0:
    ta = [0, 0]
elif len(ta) == 1:
    ta.append(0)
    print("ta: {}".format(ta))

if len(tb) == 0:
    tb = [0, 0]
    print(tb)
elif len(tb) == 1:
    tb.append(0)
    print("tb: {}".format(tb))

list_t[0] = int(ta[0]) + int(tb[0])
list_t[1] = int(ta[1]) + int(tb[1])
print(tuple(list_t))
