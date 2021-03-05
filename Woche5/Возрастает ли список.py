def IsAscending(s):
    i = 1
    while i < len(s):
        if s[i] > s[i - 1]:
            i += 1
            continue
        else:
            return "NO"
    return "YES"


s = list(map(int, input().split()))
print(IsAscending(s))
