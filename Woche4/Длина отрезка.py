from math import sqrt


def read():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x3 = float(input())
    y3 = float(input())
    return x1, y1, x2, y2, x3, y3


def d(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5


def perimetr3(x1, y1, x2, y2, x3, y3):
    distance = d(x1, y1, x2, y2) + d(x2, y2, x3, y3) + d(x1, y1, x3, y3)
    print(distance)

x1, y1, x2, y2, x3, y3 = read()
perimetr3(x1, y1, x2, y2, x3, y3)
