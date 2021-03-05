def rearrange_adjacent(s):
    for i in range(0, (len(s) // 2) * 2 - 1, 2):
        s[i], s[i + 1] = s[i + 1], s[i]

    return s


s = list(map(int, input().split()))
print(*rearrange_adjacent(s))
