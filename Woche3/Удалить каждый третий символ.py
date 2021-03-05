s = input()
i = 0
t = ""
while i < len(s):
    if i % 3 != 0:
        t += s[i]
    i += 1
print(t)
