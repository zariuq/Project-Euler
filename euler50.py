import math
import time
from itertools import izip

temp = open("primes2.txt").readlines()
primes = [int(item) for t in temp for item in t.split() if len(item) < 7]
primedic = dict((p,p) for p in primes)
lim = len(primes)

longc = 0
longp = (0,0)

for start in range(0,lim):
    total = 0
    consec = 0
    for i in range(start,lim):
        total += primes[i]
        consec += 1
        if total > 1000000:
            break
        if consec > longc:
            if primedic.has_key(total):
                longc = consec
                longp = (total,primes[start])

# Fails the 1-minute test       
        
        
        
        
       
