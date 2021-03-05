s = list(map(int, input().split()))
a = "a"
for i in range(0, len(s)):
    if s.count(s[i]) > s.count(a):
        a = s[i]
print(a)
