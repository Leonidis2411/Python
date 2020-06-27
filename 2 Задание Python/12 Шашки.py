x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
q1 = (x1 + y1) % 2
q2 = (x2 + y2) % 2

if q1 != q2:
    print('NO')
elif y1 >= y2:
    print('NO')
elif y2 - y1 < abs(x2 - x1):
    print('NO')
else:
    print('YES')
