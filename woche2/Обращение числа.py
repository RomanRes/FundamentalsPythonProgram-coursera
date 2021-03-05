n = int(input())
counter = 1
pol = 0
while counter <= n:
    test = counter
    a = 10
    la = 0
    while test != 0:
        test //= a
        a *= 10
        la += 1
    n_for = counter
    n_back = counter
    a_for, a_back = 10, 10**(la - 1)
    while n_back != 0:
        if la == 1:
            pol += 1
            break
        elif n_back // a_back != (n_for % a_for) // (a_for // 10):
            break
        n_back //= a_back
        n_for = (n_for % a_for) // (a_for / 10)
        n_back = (n_for % a_for) // (a_for / 10)
        pol += 1
    counter += 1
print(pol)
