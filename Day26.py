# Enter your code here. Read input from STDIN. Print output to STDOUT
late = input().strip().split(" ")
normal = input().strip().split(" ")
if int(late[2])>int(normal[2]):
    print(10000)
elif int(late[1]) > int(normal[1]):
    print(500*(int(late[1])-int(normal[1])))
elif int(late[0]) > int(normal[0]):
    print(15*(int(late[0])-int(normal[0])))
else:
    print(0)