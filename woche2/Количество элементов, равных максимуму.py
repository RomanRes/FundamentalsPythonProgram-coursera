n = int(input())
n_max = n
counter = 1
while n != 0:
    n = int(input())
    if n > n_max:
        n_max = n
        counter = 1
    elif n == n_max:
        counter += 1
print(counter)
