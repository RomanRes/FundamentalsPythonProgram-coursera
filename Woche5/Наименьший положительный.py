def small_positive(s):
    small = 1000
    for i in range(len(s)):
        if 0 < s[i] < small:
            small = s[i]
    return small


s = list(map(int, input().split()))
print(small_positive(s))
