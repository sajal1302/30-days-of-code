
m = int(input().strip())
for a in range(m):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    t=0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            x=i&j
            if i<j and x<k and x>t:
                t=x
    print(t)