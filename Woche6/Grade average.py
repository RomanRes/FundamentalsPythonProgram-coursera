f = open('input.txt', 'r', encoding='utf8')
grade = [0, 0, 0]
counters = [0, 0, 0]
for line in f:
    line = line.split(' ')
    if int(line[-2]) == 9:
        grade[0] += int(line[-1])
        counters[0] += 1
    elif int(line[-2]) == 10:
        grade[1] += int(line[-1])
        counters[1] += 1
    else:
        grade[2] += int(line[-1])
        counters[2] += 1
for i in range(len(grade)):
    grade[i] = grade[i] / counters[i]
print(*grade)
