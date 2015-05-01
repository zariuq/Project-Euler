

def readNames (filename):
    a1 = open(filename).readline()
    a2 = a1.split(',')
    return [a.strip('"') for a in a2]

def calcScore (string):
    sc = 0
    for l in string:
        sc += avals[l]
    return sc
    
names = readNames("p022_names.txt")
names.sort()

avals = {}

for i in range(1,27):
    avals[chr(64+i)] = i
#... I don't really need the dictionary of values... ord(l) - 64... which is faster?

colin = calcScore(names[937])

totalscore = 0
for i in range(0,len(names)):
    totalscore += (i+1) * calcScore(names[i])


