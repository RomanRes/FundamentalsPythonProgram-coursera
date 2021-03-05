def max_min(s, s_2):
    max_1, min_1 = s[0], s_2[0]
    for i in range(1, len(s)):
        if max_1 < s[i]:
            max_1 = s[i]
    for i in range(1, len(s_2)):
        if min_1 > s_2[i]:
            min_1 = s_2[i]
    return max_1, min_1


s = list(map(int, input().split()))
s_2 = s[:]
max_1, min_1 = max_min(s, s_2)
s.pop(s.index(max_1))
s_2.pop(s_2.index(min_1))
max_2, min_2 = max_min(s, s_2)
s.pop(s.index(max_2))
s_2.pop(s_2.index(min_2))
max_3, min_3 = max_min(s, s_2)
if max_1 * max_2 * max_3 > min_1 * min_2 * max_1:
    print(max_1, max_2, max_3)
else:
    print(min_1, min_2, max_1)
