s = input()
first = s.find("f", 0)
second = s.find("f", first + 1)
if first == -1:
    print(-2)
elif second == -1:
    print(second)
else:
    print(second)
