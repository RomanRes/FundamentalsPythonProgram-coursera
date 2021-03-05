myString = list(map(int, input().split()))
mySet = set()
for i in myString:
    if i in mySet:
        print("YES")
    else:
        print("NO")
    mySet.add(i)
