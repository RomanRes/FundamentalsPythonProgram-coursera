f_in = open("input.txt", 'r', encoding="utf8")
tempLines = f_in.readlines()
for line in range(len(tempLines)):
    tempLines[line] = tempLines[line].strip()
partiesList = []
counter = 1
while tempLines[counter] != "VOTES:":
    partiesList.append(tempLines[counter])
    counter += 1
counter += 1
votes = [0] * len(partiesList)
while counter <= len(tempLines) - 1:
    votes[partiesList.index(tempLines[counter])] += 1
    counter += 1
for i in range(len(partiesList)):
    partiesList[i] = [partiesList[i], votes[i]]
partiesList.sort(key=lambda a: a[0])
for i in range(len(partiesList)):
    partiesList[i].append(i)
partiesList.sort(reverse=True, key=lambda a: (a[1], -a[2]))
for i in range(len(partiesList)):
    print(partiesList[i][0])
