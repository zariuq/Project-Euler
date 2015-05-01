import math

def first_factor (num):
    for i in range (2,num):
        if num % i == 0:
            return i
    return num

divto = 20
num = 1.0

for i in range (1,divto): 
    print "iter:  " + str(i)
    if num % i != 0:
        num = num * (first_factor(i))
        print "num:  " + str(num)
        
print num
