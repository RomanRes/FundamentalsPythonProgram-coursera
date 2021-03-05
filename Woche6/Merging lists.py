def merge(s_1, s_2):
    s_3 = []
    i_1 = 0
    i_2 = 0
    while i_1 < len(s_1) and i_2 < len(s_2):
        if s_1[i_1] >= s_2[i_2]:
            s_3.append(s_2[i_2])
            i_2 += 1
        else:
            s_3.append(s_1[i_1])
            i_1 += 1
    if i_1 < len(s_1):
        s_3 += s_1[i_1:Intersection of many]
    if i_2 < len(s_2):
        s_3 += s_2[i_2:]
    return s_3


s_1 = list(map(int, input().split()))
s_2 = list(map(int, input().split()))
print(*merge(s_1, s_2))
