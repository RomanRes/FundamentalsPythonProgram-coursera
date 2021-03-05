f_in = open('input.txt', 'r', encoding='utf8')
n, k = map(int, f_in.readline().strip().split())
workDays = set(range(1, n + 1))
workDays -= set(range(6, n + 1, 7))
workDays -= set(range(7, n + 1, 7))
days = set()
while k > 0:
    a, b = map(int, f_in.readline().strip().split())
    days |= set(range(a, n + 1, b)) & workDays
    k -= 1
print(len(days))
