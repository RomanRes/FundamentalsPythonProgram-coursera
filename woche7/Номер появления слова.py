fin = open('input.txt', 'r', encoding='utf8')
myDict = dict()
line = fin.read().split()
for i in line:
    if i in myDict:
        print(myDict[i], end=" ")
        myDict[i] += 1
    else:
        print(0, end=" ")
        myDict[i] = 1
