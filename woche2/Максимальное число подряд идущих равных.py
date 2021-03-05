n = int(input())
current = n
counter1 = 0
counter2 = 1
while True:
    n = int(input())
    if n == 0:
        break
    elif n != current:
        current = n
        if counter2 > counter1:
            counter1 = counter2
            counter2 = 1
    else:
        counter2 += 1
print(counter2)
