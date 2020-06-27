a1 = str(input())
b1 = str(input())
c1 = str(input())
a2 = str(input())
b2 = str(input())
c2 = str(input())

if int(b1) < int(a1):
    (a1, b1, c1) = (b1, a1, c1)
if int(b1) > int(c1):
    (a1, b1, c1) = (a1, c1, b1)
if int(b1) < int(a1):
    (a1, b1, c1) = (b1, a1, c1)

if int(b2) < int(a2):
    (a2, b2, c2) = (b2, a2, c2)
if int(b2) > int(c2):
    (a2, b2, c2) = (a2, c2, b2)
if int(b2) < int(a2):
    (a2, b2, c2) = (b2, a2, c2)

a1 = int(a1)
b1 = int(b1)
c1 = int(c1)
a2 = int(a2)
b2 = int(b2)
c2 = int(c2)

if (a1 - a2) == 0:
    q1 = 0
else:
    q1 = (a1 - a2) / abs(a1 - a2)

if (b1 - b2) == 0:
    q2 = 0
else:
    q2 = (b1 - b2) / abs(b1 - b2)

if (c1 - c2) == 0:
    q3 = 0
else:
    q3 = (c1 - c2) / abs(c1 - c2)

s = q1 + q2 + q3

if q1 == 0 and q2 == 0 and q3 == 0:
    print('Boxes are equal')
elif s < 0 and q1 <= 0 and q2 <= 0 and q3 <= 0:
    print('The first box is smaller than the second one')
elif s > 0 and q1 >= 0 and q2 >= 0 and q3 >= 0:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
