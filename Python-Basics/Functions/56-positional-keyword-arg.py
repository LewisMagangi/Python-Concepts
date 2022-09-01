def my_func(a, b, c):
    print(a, b, c)
# using positional arguments only
my_func(12, 13, 14)

# here 1st arg is passed as positional argt while the rest as keyword argts
my_func(12, b=13, c=14)

# same as above
my_func(12, c=13, b=14)

# this is wrong as positional argument must appear before any keyword argument
# my_func(12, b=13, 14)
