a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if b != 0 and d != 0:
    if e / b == f / d and a / b == c / d:
        print("1", - a / b, a / b)
        exit()
elif b == 0 and d != 0:
    x = e / a
    y = (f - c * x) / d
    print(2, x, y)
    exit()
elif d == 0 and b != 0:
    x = f / c
    y = (e - a * x) / b
    print(2, x, y)
    exit()
elif (b * c - d * a) != 0 and (a * d - c * b) != 0:
    x = (f * b - d * e) / (b * c - d * a)
    y = (f * a - c * e) / (a * d - c * b)
    print(1, x, y)
