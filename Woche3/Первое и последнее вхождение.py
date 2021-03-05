st = input()
ts = st[::-1]
if st.find("f") != -1 and st.find("f") != len(st) - ts.find("f") - 1:
    print(st.find("f"), len(st) - ts.find("f") - 1)
elif st.find("f") != -1 and st.find("f") != -1:
    print(st.find("f"))
