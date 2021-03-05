s = list(map(int, input().split()))
count = []
for i in range(len(s)):
    if s.count(s[i]) == 1:
        count.append(s[i])
print(*count)
