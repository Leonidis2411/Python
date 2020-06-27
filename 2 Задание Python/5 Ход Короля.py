x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
q1 = abs(x1 - x2)
q2 = abs(y1 - y2)
if q1 < 2 and q2 < 2:
    print('Yes')
else:
    print('No')
