fin = open('input.txt', 'r', encoding='utf8')
num = list(fin.readline().strip())
clearNum = []
for i in range(len(num)):
    if num[i].isdigit():
        clearNum.append(num[i])
if len(clearNum) == 7:
    firstNum = ['4', '9', '5'] + clearNum
else:
    firstNum = clearNum[-10:]
for i in range(3):
    clearNum = []
    num = list(fin.readline().strip())
    first = num[0]
    for j in range(len(num)):
        if num[j].isdigit():
            clearNum.append(num[j])
    if (first == '8' or first == '+') and (len(clearNum) > 7):
        test = clearNum[-10:]
    else:
        test = ['4', '9', '5'] + clearNum[-7:]
    if test == firstNum:
        print('YES')
    else:
        print("NO")
