st = input()
print(st[:st.find("h")] + st[::-1][0:st[::-1].find("h"):1][::-1])
