n = int(input())
r = n + 1
my_sum = 0
while n > 1:
    my_sum += int(input())
    n -= 1
print(sum(range(0, r)) - my_sum)
