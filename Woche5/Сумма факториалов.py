n = int(input())
sum_fuct = 0
second = 1
for i in range(1, n + 1):
    second *= i
    sum_fuct += second
print(sum_fuct)
