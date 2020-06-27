def MinDivisor(n):
    q = 2
    while q <= int(float(n ** 0.5)):
        if n % q == 0:
            a = q
            break

        else:
            a = n
        q = q + 1
    if n == 1:
        a = ''
    elif n == 2 or n == 3:
        a = n

    return a


n = int(input())

print(MinDivisor(n))
