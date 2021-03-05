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
votesSum = sum(votes)
for i in range(len(votes)):
    if votes[i] * 100 / votesSum >= 7:
        print(partiesList[i])
