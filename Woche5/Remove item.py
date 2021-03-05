def remove_item(s, i):
    d = s[i]
    for i in range(i, len(s) - 1):
        s[i] = s[i + 1]
    s[len(s) - 1] = d
    return s


s = list(map(int, input().split()))
i = int(input())
s = remove_item(s, i)
s.pop()
print(*s)
