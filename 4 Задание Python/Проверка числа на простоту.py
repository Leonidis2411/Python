def IsPrime(n):
    kn = n ** 0.5
    a = 0
    if kn % 1 == 0:
        a = 1
    else:
        kn = int(float(n ** 0.5))
        q = 2
        while q <= kn:
            if n % q == 0:
                a = 1
                break
            q = q + 1
    return a != 1


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
