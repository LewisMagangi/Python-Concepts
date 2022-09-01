def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()
 

x = int(input("Enter a no to be fibonised: "))

fib(x) # Now call the function we just defined:
