f_in = open('input.txt', 'r', encoding='utf8')
n = int(f_in.readline())
numbers = set(range(n + 1))
numbers -= {0}
while True:
    line = f_in.readline().strip()
    if line != "HELP":
        line = set(map(int, line.split(' ')))
        if len(line) > len(numbers.intersection(line)):
            numbers &= line
            print("YES")
        else:
            numbers -= line
            print("NO")
    else:
        break
print(*sorted(numbers))
