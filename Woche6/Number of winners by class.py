f_in = open("input.txt", 'r', encoding="utf8")
classScore = [0] * 3
numWinner = [0] * 3
for line in f_in:
    line = line.split(' ')
    if int(line[2]) == 9:
        if classScore[0] < int(line[3]):
            classScore[0] = int(line[3])
            numWinner[0] = 1
        elif classScore[0] == int(line[3]):
            numWinner[0] += 1
    elif int(line[2]) == 10:
        if classScore[1] < int(line[3]):
            classScore[1] = int(line[3])
            numWinner[1] = 1
        elif classScore[1] == int(line[3]):
            numWinner[1] += 1
    else:
        if classScore[2] < int(line[3]):
            classScore[2] = int(line[3])
            numWinner[2] = 1
        elif classScore[2] == int(line[3]):
            numWinner[2] += 1
print(*numWinner)
f_in.close()
