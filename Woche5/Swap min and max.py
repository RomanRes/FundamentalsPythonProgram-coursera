s = list(map(int, input().split()))
t = s[:]
t.sort()
a, b = s.index(t[0]), s.index(t[-1])
s[s.index(t[0])], s[s.index(t[-1])] = s[s.index(t[-1])], s[s.index(t[0])]
print(*s)
