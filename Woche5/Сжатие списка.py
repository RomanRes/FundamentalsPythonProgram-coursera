s = list(map(int, input().split()))
i = len(s) - 1
while i > -1:
    if s[i] == 0:
        s.append(s.pop(i))
    i -= 1
print(*s)
