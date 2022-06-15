v = 1

def increment():
    #global v = 1   # this is error
    global v
    v = 700        # this is okay
    v = v + 1
    print(v)  # Displays 701

increment()
print(v)  # Displays 701
