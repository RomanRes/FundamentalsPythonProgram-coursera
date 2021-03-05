from math import sqrt


def sq(flag):
    n = int(input())
    if n != 0:
        sq(flag)
    if n != 0 and int(sqrt(n))**2 == n:
        flag = 1
        print(n, end=" ")
    return flag


i = sq(flag=0)
if i == 0:
    print(0)
