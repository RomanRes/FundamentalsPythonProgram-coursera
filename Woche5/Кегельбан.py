n, k = map(int, input().split())
skit = ["I"] * n
while k > 0:
    start, end = map(int, input().split())
    for i in range(start - 1, end):
        skit[i] = "."
    k -= 1
print(*skit, sep="")
