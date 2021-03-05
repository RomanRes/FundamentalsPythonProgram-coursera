from math import ceil, floor
p = float(input())
if p - int(p) >= 0.5:
    print(ceil(p))
else:
    print(floor(p))
