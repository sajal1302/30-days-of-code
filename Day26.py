a,b,c=input().split()
p,q,r=input().split()
a=int(a)
b=int(b)
c=int(c)
p=int(p)
q=int(q)
r=int(r)
if c!=r and c>r:
    print('10000')
#    exit()
elif b!=q and b>q and c>=r:
    x=(b-q)
    fine=x*500
    print(fine)
    #   break
elif a!=p and a>p and  c>=r:
    x=(a-p)
    fine=x*15
    print(fine)
    #break
else:
    print('0')