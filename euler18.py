

def readTriangle (filename):
    a1 = open(filename).readlines()
    a2 = [a.strip('\n').split(' ') for a in a1]
    return [map(int,a) for a in a2]
    

stri = readTriangle("p018_small_triangle.txt")
tri = readTriangle("p018_triangle.txt")
ltri = readTriangle("p067_triangle.txt")

t = ltri
sums = t.pop()
t.reverse()

print "sums "+str(sums)

for l in t:
    size = len(l)
    #print l
    for i in range(0,size):
        sums[i] = max(l[i] + sums[i],l[i] + sums[i+1])
    sums.pop()
    print sums
    
print sums








