import math


for b in range(1,998):
    for a in range(1,b):
        if (a + b + math.sqrt(a**2 + b**2)) == 1000:
            print str(a)+" "+str(b)







