def same_sign(s):
    i = 0
    while i < len(s) - 1:
        if (s[i] > 0 and s[i + 1] > 0) or (s[i] < 0 and s[i + 1] < 0):
            print(s[i], s[i + 1])
            break
        i += 1


s = list(map(int, input().split()))
same_sign(s)
