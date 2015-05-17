import math

def penta (n):
    return n*(3*n-1) / 2

def pplus (j,k):
    return (3*(j**2+k**2) - j - k) / 2
    
def pminus (j,k):
    return (3*(j**2-k**2) - j + k) / 2
    
def ptest (x):
    n = (math.sqrt(24*x+1)+1)/6
    if n == int(n):
        return True
    return False

ppair = []
for j in range(1000,10001):
    for k in range(1,j+1):
        if ptest(pplus(j,k)) and ptest(pminus(j,k)):
            ppair.append((j,k))
            
print ppair
