s = list(map(int, input().split()))
m = 0
index = 0
for i in range(len(s)):
    if s[i] >= m:
        m = s[i]
        index = i
print(m, index)
