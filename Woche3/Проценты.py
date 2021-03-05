p = int(input())
x = int(input())
y = int(input())
xyp = (x * 100 + y) * (100 + p) / 100
print(int(xyp // 100), int(xyp % 100))
