a = int(input())
b = int(input())
if a < b:
    print(*(range(a, b + 1)))
else:
    print(*(range(a, b - 1, -1)))
