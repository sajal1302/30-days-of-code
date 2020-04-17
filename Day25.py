import math
def prime(n): 
    if (n <= 1): 
        return False
    if (n == 2): 
        return True
    if (n > 2 and n % 2 == 0): 
        return False
    m = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + m, 2): 
        if (n % i == 0): 
            return False
    return True
n = int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
for i in a:
    if (prime(i)):
        print("Prime")
    else:
        print("Not prime")