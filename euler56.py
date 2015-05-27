# Switched to Python3...
# Ugh, dealing with bigint in c++ was a pain, so... :p

def digsum(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s
    
maxsum = ((0,0),0)

for a in range(1,100):
    if a % 10 == 0:
        continue
    ab = 1
    for b in range(1,100):
        ab = ab * a
        abdigsum = digsum(ab)
        if abdigsum > maxsum[1]:
            maxsum = ((a,b),abdigsum)
   
print(maxsum)
