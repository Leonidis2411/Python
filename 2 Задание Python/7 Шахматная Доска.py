x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
q1 = (x1 + y1) % 2
q2 = (x2 + y2) % 2
if q1 == 0 and q2 == 0:
    print('YES')
else:
    if q1 == 1 and q2 == 1:
        print('YES')
    else:
        print('NO')
