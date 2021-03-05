def key_sort(a):
    return a[1]


n = int(input())
tempList = []
for i in range(n):
    temp = input().split()
    tempList.append(temp)
for i in range(len(tempList)):
    tempList[i][1] = int(tempList[i][1])
tempList.sort(reverse=True, key=key_sort)
for i in tempList:
    print(i[0])
