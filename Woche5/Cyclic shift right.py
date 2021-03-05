def rearrange_adjacent(s):
    s.insert(0, s[-1])
    s.pop()
    return s


s = list(map(int, input().split()))
print(*rearrange_adjacent(s))
