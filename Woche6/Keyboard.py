numButtons = int(input())
tenacity = list(map(int, input().split()))
numPressed = int(input())
press = list(map(int, input().split()))
listSort = [0] * numButtons
for i in press:
    listSort[i - 1] += 1
for i in range(len(tenacity)):
    if tenacity[i] < listSort[i]:
        print("YES")
    else:
        print("NO")
