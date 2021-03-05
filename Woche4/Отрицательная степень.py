def power(a, n):
    if n == 0 and a != 0:
        return 1
    elif n == 0 and a == 0:
        return 0
    elif n < 0:
        while n != 0:
            a *= a
            n += 1
        return a
    else:
        while n > 0:
            a *= a
            n -= 1
    return a


a = float(input())
n = int(input())
print(power(a, n))
