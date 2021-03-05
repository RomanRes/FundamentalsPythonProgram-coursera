n = int(input())
if n == 1:
    print(0)
else:
    i = 2
    k = 1
    while i < n:
        i *= 2
        k += 1
    print(k)
