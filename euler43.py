import time

def addmissing (a):
    for i in range(0,10):
        if str(i) in a:
            continue
        return str(i) + a
    return a

def merge (a,b):
    return a + b[-1]
    
def mergeable (a,b):
    if a[-2:] == b[:-1]:
        if b[-1] not in a:
            return True
    return False
    
def mergeall (a,b):
    m = []
    for ai in a:
        for bi in b:
            if mergeable(ai,bi):
                m.append(merge(ai,bi))
    return m

def noduplicates (a):
    return len(a) == len(set(a))
 
t0 = time.time() 
   
divs = [2,3,5,7,11,13,17]
nums = [[],[],[],[],[],[],[]]
nums[0] = filter(noduplicates,map(str,range(100,1000,2)))

for i in range(1,7):
    if divs[i] < 10:
        nums[i] = map(lambda x: '00'+str(x),range(divs[i],10,divs[i]))
        nums[i] = nums[i] + filter(noduplicates,map(lambda x: '0'+str(x),range(divs[i]*(10/divs[i]+1),100,divs[i])))
    else:
        nums[i] = filter(noduplicates,map(lambda x: '0'+str(x),range(divs[i],100,divs[i])))
    nums[i] = nums[i] + filter(noduplicates,map(str,range(divs[i]*(100/divs[i]+1),1000,divs[i])))
    
m = map(addmissing,reduce(mergeall,nums))

answer = sum(map(int,m))
t1=time.time()
print answer
print t1-t0
# Cool, using reduce made it .02s faster!
