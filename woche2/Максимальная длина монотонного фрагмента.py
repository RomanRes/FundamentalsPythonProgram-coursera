n = int(input())
flag1 = 0
flag2 = 0
last = n
counter = 1
while True:
    n = int(input())
    if n == 0:
        break
    elif n > last and flag == 0:
        flag += 1
        n = last
    elif n < last and flag == 0:
        flag -= 1