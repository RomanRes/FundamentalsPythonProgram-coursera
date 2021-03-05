myList = list(map(int, input().split()))
sortList = [0] * 200000
for i in myList:
    sortList[i] += 1
for i in range(len(sortList)):
    print((str(i) + ' ') * sortList[i], sep=" ", end="")
