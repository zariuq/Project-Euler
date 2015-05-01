
successful_keylog = open("p079_keylog.txt").readlines()
skeys = [x.strip('\n') for x in successful_keylog] # string
        #x[0:3] works too!  But not general. 
lkeys = [ [int(x[0]),int(x[1]),int(x[2])] for x in skeys ] # list

digits = set([i for key in lkeys for i in range(0,10) if i in key])

# Ok, let's just use loops... >_>

doc = {}

for i in digits:
    if i!=0 and i !=9 and i != 8 and i != 7:
        doc[i] = {}
        for j in digits:
            if j!=0 and j !=9 and j != 8 and j != 7:
                count = 0
                for key in lkeys:
                    if i in key and j in key:
                        if key.index(i) < key.index(j):
                            count = count+1
                doc[i][j] = count
    #print str(i)+" is in front of "+str(doc[i])+" times"
    
for i in digits:
    if i!=0 and i !=9 and i != 8 and i != 7:
        print str(i)+" is in front of "+str(doc[i])+" times"
        
# Hacky
# 1) I should've removed the is from the set
# 2) I should've automated my crossing out process >_>;
