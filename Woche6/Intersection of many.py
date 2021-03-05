def Intersection(first, second):
    res = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] > second[j]:
            j += 1
        if j >= len(second) or i >= len(first):
            break
        if first[i] == second[j]:
            res.append(first[i])
            i += 1
            j += 1
        if i >= len(first) or j >= len(second):
            break
        if first[i] < second[j]:
            i += 1
    return res


s_1 = list(map(int, input().split()))
s_2 = list(map(int, input().split()))
print(*Intersection(s_1, s_2))
