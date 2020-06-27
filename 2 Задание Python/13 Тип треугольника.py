a = int(input())
b = int(input())
c = int(input())
if b < a > c:
    a1 = a
    b1 = b
    c1 = c
elif b > c:
    a1 = b
    b1 = a
    c1 = c
else:
    a1 = c
    b1 = b
    c1 = a
if b1 + c1 <= a1:
    print('impossible')
elif b1 ** 2 + c1 ** 2 == a1 ** 2:
    print('rectangular')
elif b1 ** 2 + c1 ** 2 - a1 ** 2 > 0:
    print(' acute')
elif b1 ** 2 + c1 ** 2 - a1 ** 2 < 0:
    print(' obtuse')
