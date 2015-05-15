import time
# n > 1, so at least i + 2i. And 9-digit, so 9999 is the max possible number.

t0 = time.time()
maxPan = 0
panDigits = '123456789'

# Didn't think to only search numbers starting with 9, but it makes sense given we know (9,5)...    
# Makes it 4 times faster :o
for i in ([9]+range(90,100)+range(900,1000)+range(9000,10000)):
    num = str(i) + str(i*2)
    j = 3
    l = len(num)
    while l < 10:
        if l == 9:
            if ''.join(sorted(''.join(num))) == panDigits:
                print (i,j-1)
                if num > maxPan:
                    maxPan = num
                    break
        num = num + str(i*j)
        j = j + 1
        l = len(num)

print maxPan
t1 = time.time()

print t1-t0
