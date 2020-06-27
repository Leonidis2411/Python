def power(a, n):
    k = 0
    if n < 0:
        k = -1
    if a < 0:
        return ''
    if n == 0:
        return 1
    elif n == 1:
        if a % 1 == 0:
            return int(a)
        else:
            return a
    m = a
    q = 2
    n = abs(n)
    while q <= n:
        q = q + 1
        m = m * a
    if m % 1 == 0:
        m = int(m)
    else:
        m = m

    if n > 0 and k >= 0:
        return m
    else:
        m = 1 / m
        if m % 1 == 0:
            m = int(m)
        else:
            m = m
        return m


a = float(input())
n = int(input())
rez = 0
rez = power(a, n)
print(rez)
