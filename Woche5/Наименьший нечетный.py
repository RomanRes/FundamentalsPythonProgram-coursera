def min_odd(s):
    for i in range(len(s)):
        if s[i] % 2 != 0:
            odd = s[i]
            break
    for i in range(len(s)):
        if s[i] % 2 != 0 and s[i] < odd:
            odd = s[i]
    return odd


s = list(map(int, input().split()))
print(min_odd(s))
