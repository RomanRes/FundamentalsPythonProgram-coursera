fin = open('input.txt', 'r', encoding='utf-8')
f_out = open('output.txt', 'w', encoding='utf-8')
myD = {}
vote = 0.0
for i in fin:
    myD[i.strip()] = myD.get(i.strip(), 0) + 1
    vote += 1
vote /= 2
result = sorted(myD.items(), key=lambda a: a[1], reverse=True)
print(result[0][0], file=f_out)
if result[0][1] <= vote:
    print(result[1][0], file=f_out)
