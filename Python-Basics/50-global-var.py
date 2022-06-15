global_var = 12         # a global variable

def func():
    local_var = 100     # this is local variable
    print(global_var)   # you can access global variables in side function

func()                  # calling function func()
#print(local_var)       # you can't access local_var outside the function
