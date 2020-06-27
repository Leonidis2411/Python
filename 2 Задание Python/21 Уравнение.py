a = int(input())
b = int(input())
c = int(input())
d = int(input())
x1 = abs(-b) // abs(a)
x2 = (-b) % a
x3 = a // abs(a)
x4 = b // abs(b)
if b == 0 and d == 0:
    print('NO')
elif x2 != 0:
    print('NO')
elif (c * x1 * x3 * (-x4) + d) == 0:
    print('NO')
else:
    x5 = x1 * x3 * (-x4)
    print(str(x5))
