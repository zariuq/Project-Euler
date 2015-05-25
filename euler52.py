import math
import time

def multest (n,x):
    digits = sorted(str(n))
    for i in range(2,x+1):
        if digits != sorted(str(i*n)):
            return False
    return True
    
test = 125874
answer = 0

i = 1
while not multest(i,6):
    i += 1
answer = i

# Passes the 1min test




