def func(i, n = 100):
    print(i, n)

func(2) #  here no value is passed to n, so default value will be used
func(2, 30) # here 30 is passed as a value of n, so default value isn't be used
