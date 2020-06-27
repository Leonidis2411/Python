a = int(input())
b = int(input())
c = int(input())
a1 = a % 2
b1 = b % 2
c1 = c % 2
s1 = a1 + b1 + c1
if 3 > s1 > 0:
    print('YES')
else:
    print('NO')
