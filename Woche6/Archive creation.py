s, counter = map(int, input().split())
d_space = []
while counter > 0:
    d_space.append(int(input()))
    counter -= 1
d_space.sort(reverse=True)
users = 0
i = len(d_space) - 1
while i >= 0:
    s -= d_space[i]
    i -= 1
    if s >= 0:
        users += 1
    else:
        break
print(users)
