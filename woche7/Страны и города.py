fin = open('input.txt', 'r', encoding='utf8')
n = int(fin.readline().strip())
myDict = dict()
for i in range(n):
    line = list(fin.readline().strip().split())[::-1]
    for elm in range(len(line) - 1):
        myDict[line[elm]] = line[-1]
m = int(fin.readline().strip())
for i in range(m):
    print(myDict[fin.readline().strip()])
