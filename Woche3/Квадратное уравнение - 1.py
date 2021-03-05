a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c
if a == 0 and b == 0 and c != 0:
    print(0)
    exit(0)
elif a == 0 and b == 0 and c == 0:
    print(3)
    exit(0)
elif d < 0:
    print(0)
    exit(0)
elif a == 0:
    print('1', -c / b)
    exit(0)
x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)
if x1 > x2:
    x1, x2 = x2, x1
if d == 0:
    print(1, x1)
elif d > 0:
    print(2, x1, x2)
else:
    print(0)
