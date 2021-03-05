f_in = open("input.txt", "r", encoding="utf8")
n = int(f_in.readline())
tempList = f_in.readlines()
for i in range(len(tempList)):
    tempList[i] = tempList[i].strip().split()
past = []
for i in range(len(tempList)):
    tempList[i][-3:] = map(int, tempList[i][-3:])
    a, b, c = tempList[i][-1], tempList[i][-2], tempList[i][-3]
    if a < 40 or b < 40 or c < 40:
        continue
    else:
        past.append(tempList[i])
# proverka 0
if len(past) <= n:
    print(0)
    exit(0)
# proverka 1
past.sort(reverse=True, key=lambda a: sum(a[-3:]))
counter = 0
while counter < len(past) < sum(past[counter][-3:]) == sum(past[0][-3:]):
    counter += 1
if counter > n:
    print(1)
    exit(0)
# print prohodnogo bala
counter = n
while counter > 0 and (sum(past[n][-3:]) == sum(past[counter - 1][-3:])):
    counter -= 1
past = past[:counter]
print(sum(past[-1][-3:]))
