import math

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# So, fuck, my problems were twofold: 
#    1) My factor checking was slow.
#    2) My thinking led me to overshoot, goddamnit--


tnum = 1
l = len(factors(tnum))
i = 2

while l < 500:
    tnum = tnum + i
    i = i + 1
    l = len(factors(tnum))

print "divisors: " + str(l)
print "triangle num: " + str(tnum)
