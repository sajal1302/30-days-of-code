n = int(input())

f = 0
count = 0

while n != 0:
    fact= n // 2
    rem = n - 2 * fact
    n = fact
    if rem == 1:
        count += 1
        f = max(f, count)
    else:
        count = 0

print(f)
