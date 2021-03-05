def insert_items(s, k, c):
    s.append(0)
    for i in range(len(s) - 1, k, -1):
        s[i] = s[i - 1]
    s[k] = c
    return s


s = list(map(int, input().split()))
k, c = map(int, input().split())
print(*insert_items(s, k, c))
