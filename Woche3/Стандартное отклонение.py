x = int(input())
n = 0
x_sum_2 = x ** 2
x_sum = x
while x != 0:
    x = int(input())
    x_sum += x
    x_sum_2 += x ** 2
    n += 1
s = x_sum / n
print(((x_sum_2 + n * (s ** 2) - 2 * s * x_sum) / (n - 1))**0.5)
