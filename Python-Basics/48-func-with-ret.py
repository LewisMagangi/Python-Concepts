def sum(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    return result  # The return statement sends a result back to the caller.

s = sum(10, 50)
print(s)
