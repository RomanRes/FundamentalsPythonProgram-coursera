def nearest_number(n, s, a):
    distance = 2001
    min_n = 3001
    for i in range(len(s)):
        if a >= 0 and s[i] >= 0 and abs(s[i] - a) < distance:
            distance = abs(s[i] - a)
            min_n = s[i]
        elif a < 0 and s[i] < 0 and abs(s[i] - a) < distance:
            distance = abs(s[i] - a)
            min_n = s[i]
        elif a >= 0 and s[i] < 0 and abs(s[i] - a) < distance:
            distance = abs(s[i] - a)
            min_n = s[i]
        elif a < 0 and s[i] >= 0 and abs(s[i] - a) < distance:
            distance = abs(-s[i] + a)
            min_n = s[i]
    return min_n


n = int(input())
s = list(map(int, input().split()))
a = int(input())
print(nearest_number(n, s, a))
