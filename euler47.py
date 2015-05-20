import math
import time

temp = open("primes2.txt").readlines()
primes = [int(item) for t in temp for item in t.split()]

#Hmm, damnit, adding the prime factors as part of doing a sieve may be faster
def pf (n):
    fs = {}
    i = 0
    while n > 1:
        if n % primes[i] == 0:
            n /= primes[i]
            fs[primes[i]] = 1 + fs.get(primes[i],0)
            if n > 1: #significant speed boost =D (well, when you get over 100,000)
                updatewith(fs,pfs[n])
                break
        else:
            i+=1
    return fs
    
def updatewith(dic1,dic2):
    for item in dic2.items():
        dic1[item[0]] = item[1] + dic1.get(item[0],0)

def distinct(n1,n2):
    for item in n1.items():
        if item[1] == n2.get(item[0],0):
            return False
    return True

t0 = time.time()    

pfs = [{0:1},{1:1}]

# Adding these AS I GO would be better. Add the first 6, and then just add as I go? Yeah.
for i in range(2,150000):
    pfs.append(pf(i))
  
  
for i in range(2,150000):
    if len(pfs[i]) == 4 and len(pfs[i+1]) == 4 and len(pfs[i+2]) == 4 and len(pfs[i+3]) == 4:
        print i
        if distinct(pfs[i],pfs[i+1]) and distinct(pfs[i+1],pfs[i+2]) and distinct(pfs[i],pfs[i+1]) and distinct(pfs[i],pfs[i+3]) and distinct(pfs[i+1],pfs[i+3]) and distinct(pfs[i+2],pfs[i+3]):
            print "answer:"
            print str(i) + str(pfs[i])
            print str(i+1) + str(pfs[i+1])
            print str(i+2) + str(pfs[i+2])
            print str(i+3) + str(pfs[i+3])
            break
    
    
    
    
    
t1 = time.time()

print "time: " + str(t1-t0)
