tempBus = list(map(int, input().split()))
bus1 = sorted(tempBus[:2])
bus2 = sorted(tempBus[2:])
set1 = set(range(bus1[0], bus1[1] + 1))
set2 = set(range(bus2[0], bus2[1] + 1))
print(len(set1 & set2))
