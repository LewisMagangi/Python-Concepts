# Python program to demonstrate finally

# Exception is not handled
try:
        kikko = 50584 // 0 # exception raised
        print(kikko)

finally:
        # this block is always executed
        # regardless of exception generation.
        print('This is always executed') 
