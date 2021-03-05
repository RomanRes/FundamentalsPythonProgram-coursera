a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a - c) % 2 == 0 and (b - d) % 2 == 0:
    print("YES")
elif (a - c) % 2 == 1 and (b - d) % 2 == 1:
    print("YES")
else:
    print("NO")
