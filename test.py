from math import sqrt

t = int(input())
while t > 0:
    res = 10000000000000000000
    a = -1
    b = -1
    t -= 1
    s = int(input())
    for n in range(1, int(sqrt(s))):
        m = (2 * s - n - 1) / (2 * n + 1)
        if m != int(m):
            continue
        temp = n - m
        if (temp < res):
            res = temp
            a = int(n)
            b = int(m)
    print(a, b)
        