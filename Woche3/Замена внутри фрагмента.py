s = input()
t = s[s.find("h") + 1: s.rfind("h")]
while t.find("h") != -1:
    t = t.replace("h", "H")
print(s[0:s.find("h") + 1] + t + s[s.rfind("h"):])
