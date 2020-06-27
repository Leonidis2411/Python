N = int(input())
M = int(input())
a1 = M // N
a2 = (M) % (-N)
a3 = (-M) % (-N)
a4 = (a2 + a3) // (-N)
a12=(N) % (-M)
a13=(-N) % (-M)
a14=(a12+a13)//(-M)
a1=1
a5 = a1 + 1 * a4
print(str(a5))
