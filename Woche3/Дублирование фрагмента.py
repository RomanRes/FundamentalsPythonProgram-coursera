st = input()
print(st[0:st.find("h") + 1], end="")
print(2 * st[st.find("h") + 1:len(st) - st[::-1].find("h") - 1], end="")
print(st[len(st) - st[::-1].find("h") - 1:], end="")
