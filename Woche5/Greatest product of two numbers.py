s = list(map(int, input().split()))
max_1, max_2 = s[0], s[1]
min_1, min_2 = s[0], s[1]
if max_1 < max_2:
    max_1, max_2 = max_2, max_1
if min_1 > min_2:
    min_1, min_2 = min_2, min_1
for i in range(2, len(s)):
    if s[i] >= max_2:
        max_1, max_2 = s[i], max_1
        if max_1 < max_2:
            max_1, max_2 = max_2, max_1
    if s[i] <= min_2:
        min_2 = s[i]
        if min_1 > min_2:
            min_1, min_2 = min_2, min_1
if min_1 * min_2 > max_1 * max_2:
    print(min_1, min_2)
else:
    print(max_2, max_1)
