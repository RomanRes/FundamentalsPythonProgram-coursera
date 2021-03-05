def number_diff_elem(s):
    counter = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            counter += 1
            i += 1
    return counter + 1


s = list(map(int, input().split()))
print(number_diff_elem(s))
