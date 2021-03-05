listKM = list(map(int, input().split()))
listPrice = list(map(int, input().split()))
listKM.sort()
listPrice.sort(reverse=True)
sumPrice = 0
for i in range(len(listKM)):
    sumPrice += listKM[i] * listPrice[i]
print(sumPrice)
