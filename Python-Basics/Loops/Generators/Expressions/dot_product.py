"""
sums the respective index value of each list
"""
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec))) 
