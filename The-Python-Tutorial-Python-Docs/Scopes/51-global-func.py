tx = 1

def increment():
    global tx  # now t inside the function is same as t outside the function
    tx = tx + 1
    print(tx)  # Displays 2

increment()
print(tx)  # Displays 2
