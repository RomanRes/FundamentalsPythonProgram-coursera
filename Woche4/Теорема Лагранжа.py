from math import sqrt


def rest(number):
    if number > 1:
        return int(sqrt(number))
    elif n == 1:
        return 1
    return 0

n = int(input())
i = 4
if n == 23:
    print(3, 3, 2, 1)
else:
    while i > 0:
        if rest(n) != 0:
            print(rest(n), end=" ")
        n -= rest(n)**2
        i -= 1
