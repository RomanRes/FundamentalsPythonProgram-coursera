n = int(input())
i = 1
s = 0
while n > 0:
    s += (1 / i**2)
    n -= 1
    i += 1
print(s)
