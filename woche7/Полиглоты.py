f_in = open("input.txt", "r", encoding="utf8")
n = int(f_in.readline())
language = set()
comLanguages = set()
for i in range(int(f_in.readline())):
    tempLang = f_in.readline().strip()
    comLanguages.add(tempLang)
    language.add(tempLang)
while n - 1 > 0:
    temp = int(f_in.readline())
    tempSet = set()
    for i in range(temp):
        tempLang = f_in.readline().strip()
        language.add(tempLang)
        tempSet.add(tempLang)
    comLanguages &= tempSet
    n -= 1
print(len(comLanguages))
for i in comLanguages:
    print(i)
print(len(language))
for i in language:
    print(i)
