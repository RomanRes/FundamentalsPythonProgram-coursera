def read():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    return a, b, c, d


def min4():
    a, b, c, d = read()
    print(min(a, b, c, d))


min4()
