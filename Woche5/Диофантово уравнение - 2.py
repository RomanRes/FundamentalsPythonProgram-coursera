a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
count = 0
for x in range(0, 1001):
    y = a * x**3 + b * x**2 + c * x + d == 0
    if y and x - e != 0:
        count += 1
print(count)
