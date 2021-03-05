first_apart = int(input())
last_apart = int(input())
if (first_apart - 1) % (last_apart - first_apart + 1) != 0:
    print("NO")
else:
    print("YES")
