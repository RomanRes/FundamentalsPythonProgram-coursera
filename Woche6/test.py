from collections import namedtuple
from typing import Type

'''
class Man:
    height = 0
    name = ""


def sortMan(man):
    return -man.height, man.name


n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    man = Man()
    man.height = int(tempManData[0])
    man.name = tempManData[1]
    peopleList.append(man)
    peopleList.sort(key=sortMan)
for man in peopleList:
    print(man.height, man.name)
    
n = int(input())
peopleNametuple = []
Man = namedtuple('Man', ["height", 'name'])
for i in range(n):
    temp = input().split()
    man = Man(int(temp[0]), temp[1])
    peopleNametuple.append(man)
for i in peopleNametuple:
    print(i.height, i.name)


print(' '.join(map(lambda x: str(x**2), range(1, 101))))
'''
marks = map(int, input().split())
cntMarks = [0] * 11
for mark in marks:
    cntMarks[mark] += 1
for nowMark in range(11):
    print((str(nowMark) + ' ') * cntMarks[nowMark], end='')