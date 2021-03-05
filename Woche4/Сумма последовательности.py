def sequence():
    n = int(input())
    if n != 0:
        return n + sequence()
    return n


print(sequence())
