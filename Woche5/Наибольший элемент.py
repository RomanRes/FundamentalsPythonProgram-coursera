def max_number(a):
    max_n = a[0]
    index = 0
    for i in range(len(a)):
        if a[i] > max_n:
            max_n = a[i]
            index = i
    return max_n, index


s = list(map(int, input().split()))
print(*max_number(s))
