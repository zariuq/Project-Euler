import math

def penta (n):
    return n*(3*n-1) / 2
    
def tri (n):
    return n*(n+1) / 2
    
def hexa (n):
    return n*(2*n-1)

def ttest (x):
    n = (math.sqrt(8*x + 1) - 1) / 2
    if n == int(n):
        return int(n)
    return False

def ptest (x):
    n = (math.sqrt(24*x+1)+1)/6
    if n == int(n):
        return int(n)
    return False
    
# hexa(143) is all threee. Find next.

answer = 0
for i in range(144,123400):
    m = hexa(i)
    if ptest(m):
        answer = m
        break

print answer     
