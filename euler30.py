
def digpowsum (a, p):
    s = 0
    for i in str(a):
        s += int(i)**p
    return s

ans = []    
for i in range(10,354294): #9**5 * 6 is six digits, an upper limit
    t = digpowsum(i,5)
    if t == i:
        ans.append(i)

print ans
print sum(ans)
    
    
    
