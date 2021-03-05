def my_sum(a, b):
    if a != 0:
        return my_sum(a - 1, b + 1)
    return b


a = int(input())
b = int(input())
print(my_sum(a, b))
