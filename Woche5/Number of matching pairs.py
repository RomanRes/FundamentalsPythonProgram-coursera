s = list(map(int, input().split()))
pair = 0
while len(s) > 1:
    for i in range(1, len(s)):
        if s[0] == s[i]:
            pair += 1
    s.pop(0)
print(pair)
