a = float(input())
n = int(input())


def my_pow(a, n):
    while n > 0:
        return a * pow(a, n - 1)
    return a


print(pow(a, n))
