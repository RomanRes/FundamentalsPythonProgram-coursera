x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 <= x2) and (y1 <= y2):
    if ((x1 + x2) % 2 == 0) and ((y1 + y2) % 2 == 0):
        print("YES")
    elif ((x1 + x2) % 2 == 1) and ((y1 + y2) % 2 == 1):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
