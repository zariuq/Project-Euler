from fractions import Fraction
import time

t0 = time.time()
curiousFractions = []

for c in range(1,10):
    for a in range(1,c):
        singleFraction = float(a)/c
        for b in range (1,10):
            if float(str(a)+str(b)) / float(str(b)+str(c)) == singleFraction:
                curiousFractions.append( (str(a)+str(b), str(b)+str(c)) )
            if float(str(b)+str(a)) / float(str(c)+str(b)) == singleFraction:
                curiousFractions.append( (str(b)+str(a), str(c)+str(b)) )

t2 = time.time()
print curiousFractions
fracMult = lambda x : float(x[0])/float(x[1])
curiousDecimals = map(fracMult,curiousFractions)
product =  reduce(lambda x, y: x * y, curiousDecimals)
print Fraction(product).limit_denominator()
t1 = time.time()

print t1-t0
print t2-t0

# Hmma, I could've done more of it with fractions!... Oh well :p






