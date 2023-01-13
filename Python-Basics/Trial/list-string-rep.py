mylist = "Best School"
x = (list(mylist))

for i in range (0, len(x) - 1):
    if x[i] == "o":
        x[i] = ""
print("".join(x))

