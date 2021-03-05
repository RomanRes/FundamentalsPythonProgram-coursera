f_in = open("input.txt", "r", encoding="utf8")
school = [0] * 100
for line in f_in:
    line.strip()
    tempLine = line.split()
    school[int(tempLine[-2])] += 1
maxSchool = max(school)
for i in range(len(school)):
    if school[i] == maxSchool:
        print(i, end=" ")
