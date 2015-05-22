import math
import time

temp = open("primes2.txt").readlines()
primes = [item for t in temp for item in t.split() if len(item) == 4]

permprime = {}

for p in primes:
    slot = ''.join(sorted(p))
    permprime[slot] = [p] + permprime.get(slot,[])

for it in permprime.keys():
    if len(permprime[it]) < 3:
        del permprime[it]
    else:
        permprime[it].sort()

for it in permprime.values():
    size = len(it)
    diff = []
    for i in range(0,size-1):
        diff.append(int(it[i+1])-int(it[i]))
    for i in range(0,len(diff)-1):
        if diff[i] == diff[i+1]:
            print it[i:]
            
# Wait... it finds the answer, but not the sample I was given.
# If there's a number in-between them, it won't find them. 
# So I'd have to computer ALL differences in an anagram group and see if any two are the same with the one in the middle being identical.
# Heh, half-assed code can work -.-;
