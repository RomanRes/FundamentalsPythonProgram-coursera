file = open("input.txt", "r", encoding="utf8")
lines = file.readlines()


class List_Winners:
    win9 = []
    win10 = []
    win11 = []


for i in lines:
    i = i.strip()
    i = i.split(" ")
    if int(i[-2]) == 9:
        List_Winners.win9.append(i)
    elif int(i[-2]) == 10:
        List_Winners.win10.append(i)
    else:
        List_Winners.win11.append(i)
List_Winners.win9.sort(reverse=True, key=lambda a: int(a[-1]))
List_Winners.win10.sort(reverse=True, key=lambda a: int(a[-1]))
List_Winners.win11.sort(reverse=True, key=lambda a: int(a[-1]))
for i in List_Winners.win9:
    if int(i[-1]) != int(List_Winners.win9[0][-1]):
        print(i[-1], end=" ")
        break
for i in List_Winners.win10:
    if int(i[-1]) != int(List_Winners.win10[0][-1]):
        print(i[-1], end=" ")
        break
for i in List_Winners.win11:
    if int(i[-1]) != int(List_Winners.win11[0][-1]):
        print(i[-1], end=" ")
        break
file.close()
