n = int(input())
a, b, c, d = "", "", "", ""
for i in range(1, n + 1):
    a += "+___ "
    b += "|{} / ".format(i)
    c += "|__\ "
    d += "|    "
print(a)
print(b)
print(c)
print(d)
