fin = open('input.txt', 'r', encoding='utf8')
myDict = dict()
for line in fin:
    line = line.strip().split()
    myDict[line[0]] = myDict.get(line[0], 0) + int(line[1])
for i in sorted(myDict):
    print(i, myDict[i])
