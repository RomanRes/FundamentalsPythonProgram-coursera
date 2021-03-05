f_in = open('input.txt', 'r', encoding="utf8")
n, m = map(int, f_in.readline().strip().split(' '))
tempColors = list(map(int, f_in.readlines()))
colors_N = tempColors[:n]
colors_M = tempColors[n:]
print(len(set(colors_N) & set(colors_M)))
print(*sorted(set(colors_N) & set(colors_M)))
print(len(set(colors_N) - (set(colors_N) & set(colors_M))))
print(*sorted(set(colors_N) - (set(colors_N) & set(colors_M))))
print(len(set(colors_M) - (set(colors_N) & set(colors_M))))
print(*sorted(set(colors_M) - (set(colors_N) & set(colors_M))))
