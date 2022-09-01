def foo():
    global i   # i is declared as global so it is available outside the function
    i = 100

foo()
print(i)
