import math

# So, for many problems, I'll need to find a list of many primes -_-;

primes = [2]

def is_prime (n):
    if n == 1: # 1 isn't prime
        return False
    elif n < 4: # 2/3
        return True
    elif n % 2 == 0: # no evens
        return False
    elif n < 9: # 5,7
        return True
    elif n % 3 == 0: # 2 and 3 gets most gaps...
        return False
    else:
        r = int(math.floor(math.sqrt(n)))
        for f in primes:
            if f > r:
                return True
            elif n % f == 0:
                return False
        return True

# For problem 12
count = 1
p = 1
while count < 500:
    if is_prime(p):
        primes.append(p)
        count = count + 1
    p=p+2

# For Problem 11
#for p in range(1,2000000,2):
#    if is_prime(p):
#        primes.append(p)
        
#print "/nEnd of loop/n"
       
print primes

#print sum(primes)
