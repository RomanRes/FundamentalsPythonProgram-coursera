n = int(input())
f0 = 0
f1 = 1
counter = 1
while f1 < n:
    if n == 1:
        print(f1)
    f0, f1 = f1, f0 + f1
    counter += 1
if f1 == n and n != 0:
    print(counter)
elif n == 0:
    print(0)
else:
    print(-1)
