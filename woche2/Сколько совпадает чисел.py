a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print(3)
elif a == c or b == c or a == b:
    print(2)
else:
    print(0)
