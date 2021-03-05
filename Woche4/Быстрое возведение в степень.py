def my_pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return my_pow(a * a, n // 2)
    else:
        return a * my_pow(a, n - 1)
    return a


a = float(input())
n = int(input())
print(my_pow(a, n))
