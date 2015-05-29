import math
'''
temp = open("primes-1000000000.txt").readlines()
#temp = open("primes2.txt").readlines()

def getprimes (tem):
    primeslist = []
    for t in tem:
        for item in t.split():
            if len(item) > 9:
                return primeslist
            primeslist.append(int(item))
    return primeslist
            
primes = getprimes(temp)
'''

#pdic = dict((i,1) for i in primes)

# So, testing 40,000 primes is MUCH faster than loading 50,000,000! xDDD

def is_prime(p):
    sq = math.sqrt(p)
    for i in range(2,int(sq)+1):
        if (p % i == 0):
            return 0
    return 1

pnum = 0
tot = 1
per = 1
cur = 1
s = 0

while per > 0.1:
    s += 2
    for i in range(4):
        cur += s
        pnum += is_prime(cur)
        #print(cur,end=' ')
    tot += 4
    per = pnum / tot
    #print()
    
print(s+1)

