s = int(input())
e = int(input())
for i in range(s, e + 1):
    i = str(i)
    if i[0] == i[-1] and i[1] == i[-2]:
        print(i)
