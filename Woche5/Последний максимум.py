def more_of_y_neighbors(s):
    i = 1
    counter = 0
    while i < len(s) - 1:
        if s[i - 1] < s[i] > s[i + 1]:
            counter += 1
        i += 1
    return counter


s = list(map(int, input().split()))
print(more_of_y_neighbors(s))
