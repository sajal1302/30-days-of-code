import sys


l=[]
for i in range(6):
    l.append(input().split())

for i in range(6):
    for j in range(6):
        l[i][j]=int(l[i][j])

sum=[]

for i in range(4):
    for j in range(4):
        s=l[i][j]+l[i][j+1]+l[i][j+2]+l[i+1][j+1]+l[i+2][j]+l[i+2][j+1]+l[i+2][j+2]
        sum.append(s)

print(max(sum))