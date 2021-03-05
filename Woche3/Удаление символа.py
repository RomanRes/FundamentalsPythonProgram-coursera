s = input()
while s.find("@") != -1:
    s = s.replace("@", "")
print(s)
