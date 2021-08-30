import random

D = 9
M = 7
while M == 8 and D == 31:
    number = random.randint(100, 120)
    if D < 31:
        D = D + 1
    else:
        M = M + 1
        D = 1
    print('%s月%s日: %s' % (M, D, number))
