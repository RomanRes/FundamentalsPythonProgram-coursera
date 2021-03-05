def stand_in_line(s, n):
    i = 0
    s.append(0)
    while s[i] >= n:
        i += 1
    return i + 1


s = list(map(int, input().split()))
n = int(input())
print(stand_in_line(s, n))
