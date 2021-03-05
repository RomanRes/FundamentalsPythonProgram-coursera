n = int(input())
if n == 0:
    print("NO")
elif n == 1:
    print("YES")
elif n == 2:
    print("YES")
else:
    i = 2
    while True:
        i *= 2
        if i > n:
            print("NO")
            break
        elif i == n:
            print("YES")
            break
