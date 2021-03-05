fin = open('input.txt', 'r', encoding="utf8")
text = fin.read().strip().split()
myD = {}
for i in text:
    myD[i] = myD.get(i, 0) + 1
myList = sorted(myD.items(), key=lambda a: (-a[1], a[0]))
print(myList[0][0])
