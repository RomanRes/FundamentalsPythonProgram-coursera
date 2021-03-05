s = input()
t = s[1:].replace("", "*", s.count("") - 2)
print(s[0] + t)
