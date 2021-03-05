a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (c == a - 1) and (b == d or d == b - 1 or d == b + 1):
    print("YES")
elif (c == a) and (b == d or d == b - 1 or d == b + 1):
    print("YES")
elif (c == a + 1) and (b == d or d == b - 1 or d == b + 1):
    print("YES")
else:
    print("NO")
