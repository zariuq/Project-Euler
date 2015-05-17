def getv (w):
    v = 0
    for l in w:
        v = v + lv[l]
    return v

def trinum (n):
    return n*(n+1)/2
    
wordstemp = open("p042_words.txt").readline()
words = eval("["+wordstemp+"]")  

# >_> Made via for loop
lv = {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26}

wv = {}

for word in words:
    v = getv(word)
    wv[v] = wv.get(v,[]) + [word]
    
# MAX VALUE = 192

i = 1
ti = trinum (i)
twords = 0
while ti < 192:
    twords += len(wv.get(ti,[]))
    i += 1
    ti = trinum(i)
    
print twords
