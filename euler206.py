import math

test = "1234567890"
lower_bound = 1020304050607080900
lower_sq = int(math.sqrt(lower_bound))
upper_bound = 1929394959697989990
upper_sq = int(math.sqrt(upper_bound)) + 1

def is_match(n):
    s = str(n)
    for i in range(0,10):
        if s[2*i] != test[i]:
            return False
    return True
'''       
for i in range(lower_sq,upper_sq,10):
    k = int(i**2)
    if is_match(k):
        print(k)
        break
'''

q = 1929374254627488900
answer = 1389019170

# -_- Goddamnit, python is slow as a cow's uncle, but it found it.
# c++ must've been squaring in Double and losing some digits as it converted to long int or something.
# Since my seemingly identical code there didn't find it :o





