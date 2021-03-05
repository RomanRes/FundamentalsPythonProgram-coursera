def gcd(a, b):
    while b > 0:
        return gcd(b, a % b)
    return a


def ReduceFraction(n, m):
    return n // gcd(n, m), m // gcd(n, m)


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
