fin = open('input.txt', 'r', encoding='utf8')
myD = {}
for i in range(int(fin.readline())):
    line = fin.readline().strip().split()
    myD[line[1]] = line[0]
    myD[line[0]] = line[1]
print(myD[fin.readline().strip()])
