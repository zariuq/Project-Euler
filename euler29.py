p = {}
for a in range (2,100+1):
    for b in range (2,100+1):
        t = a**b
        p[t] = p.get(t,[])+[(a,b)] 
        
print len(p)  
