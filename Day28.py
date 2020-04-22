
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
names = []
for _ in range(n):
    name, email = input().rstrip().split()
    if(email.endswith('@gmail.com')):
        names.append(name)
names.sort()
for name in names:
    print(name)