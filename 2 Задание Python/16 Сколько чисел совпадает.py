a = int(input())
b = int(input())
c = int(input())
q1 = b - a
q2 = c - a
q3 = c - b
if q1 != 0:
    q1 = 1
if q2 != 0:
    q2 = 1
if q3 != 0:
    q3 = 1
s = q1 + q2 + q3
if s == 3:
    print('0')
if s == 0:
    print('3')
if s == 2:
    print('2')
