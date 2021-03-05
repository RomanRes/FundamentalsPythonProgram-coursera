n = int(input())
n1_max = 0
n2_max = n
while n != 0:
    n = int(input())
    if n1_max < n <= n2_max:
        n1_max = n
    elif n > n2_max:
        n1_max = n2_max
        n2_max = n
print(n1_max)
