p = int(input())
x = int(input())
y = int(input())
k = int(input())
while k > 0:
    xyp = (x * 100 + y) * (100 + p) / 100
    x = int(xyp // 100)
    y = int(xyp % 100)
    k -= 1
print(x, y)
