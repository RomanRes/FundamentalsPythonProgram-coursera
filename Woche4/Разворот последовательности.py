def sequence():
    n = int(input())
    if n != 0:
        sequence()
    print(n)


sequence()
