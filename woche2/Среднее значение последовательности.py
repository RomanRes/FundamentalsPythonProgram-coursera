sum_counter = 0
counter = 0
while True:
    n = int(input())
    if n == 0:
        print(sum_counter / counter)
        break
    sum_counter += n
    counter += 1
