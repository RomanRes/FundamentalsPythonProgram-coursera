def IsPointInSquare(x, y):
    r = ((x + 1)**2 + (y - 1)**2)**0.5 <= 2
    r_not = ((x + 1) ** 2 + (y - 1) ** 2) ** 0.5 >= 2
    a = (x + y >= 0 and 2 + 2 * x - y <= 0)
    b = (x + y <= 0 and 2 + 2 * x - y >= 0)
    return (r and a) or (r_not and b)


x = float(input())
y = float(input())

if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
