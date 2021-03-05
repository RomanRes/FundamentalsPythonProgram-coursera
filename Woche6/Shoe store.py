n = int(input())
s = list(map(int, input().split()))
s.sort()
i = 0
while i <= (len(s) - 1) and s[i] < n:
    i += 1
s = s[i:]
if len(s) != 0:
    pars = 1
    last = s[0]
    for i in range(len(s)):
        if s[i] - last >= 3:
            last = s[i]
            pars += 1
    print(pars)
else:
    print(0)
