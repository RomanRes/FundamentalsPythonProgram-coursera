a = int(input())
b = int(input())
c = int(input())
if a <= b:
    if b >= c:
        print(b)
    else:
        print(c)
elif a >= b:
    if c >= a:
        print(c)
    else:
        print(a)
