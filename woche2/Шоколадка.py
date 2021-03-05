n = int(input())
m = int(input())
k = int(input())
if n * m <= k:
    print("NO")
elif (n <= k) or (m <= k):
    if (k % n == 0) or (k % m == 0):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
