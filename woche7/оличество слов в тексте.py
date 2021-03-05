f_in = open('input.txt', 'r', encoding="utf8")
print(len(set(f_in.read().split())))
