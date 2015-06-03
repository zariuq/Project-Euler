count = 0;

print("initiating...")

# len(str(9**22)) == 21, so 21 is the limit.
for n in range (1,22):
    i = 1
    p = pow(i,n)
    l = len(str(p))
    while len(str(p)) <= n:
        if l == n:
            print(str(i)+"^"+str(n)+" =", p)
            count += 1
        i += 1
        p = pow(i,n)
        l = len(str(p))

print("There are", count)
