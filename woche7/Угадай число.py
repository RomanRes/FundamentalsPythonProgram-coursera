f_in = open('input.txt', 'r', encoding='utf8')
n = int(f_in.readline())
numbers = set(range(n + 1))
numbers -= {0}
while True:
    line = f_in.readline().strip()
    if line != "HELP":
        line2 = f_in.readline().strip()
        line = set(map(int, line.split(' ')))
        if line2 == "YES":
            numbers &= line
        else:
            numbers -= line
    else:
        break
print(*sorted(numbers))
