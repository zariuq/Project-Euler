
bigN = 5

def permBranch (n, xs):
    if n == 0:
        return [xs]
    return permBranch(n-1,'0'+xs)+permBranch(n-1,'1'+xs)

def continues (x1, x2):
    return x1[1:] == x2[:-1]

a3 = permBranch(bigN, "")

print a3
print 'continues "123" "234" = '+str(continues("123","234"))

fix = [a3[0]]
a3 = a3[1:]

'''
for i in range(0,2**bigN - 1):
    print fix
    if fix[-1][1:]+'1' in a3:
        a3.remove(fix[-1][1:]+'1')
        fix.append(fix[-1][1:]+'1')
    elif fix[-1][1:]+'0' in a3:
        a3.remove(fix[-1][1:]+'0')
        fix.append(fix[-1][1:]+'0')
        
print fix
'''

anslist = [] # list of lists


#a3, fix, anslist, depth
def recans (a, f, an, d):
    if len(f) == d:
        answer = ''
        for s in f:
            answer = answer + s[0]
        an.append(answer)
        return
    if f[-1][1:]+'1' in a:
        p = f[-1][1:]+'1'
        i = a.index(p)
        recans(a[:i]+a[i+1:],f+[a[i]],an, d)
    if f[-1][1:]+'0' in a:
        p = f[-1][1:]+'0'
        i = a.index(p)
        recans(a[:i]+a[i+1:],f+[a[i]],an, d)
    
    return

recans(a3,fix,anslist, 2**bigN)

sumy = 0
for i in anslist:
    sumy += int(i,2)
    
print sumy


