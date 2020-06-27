a = float(input())
b = float(input())
c = float(input())
q = 0
ds = 0
x1 = 0
x2 = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0
ln = 0
ln1 = 0
ln2 = 0
ost = 0
ost1 = 0
ost2 = 0
q11 = 0
q12 = 0
q13 = 0
q14 = 0
q15 = 0
q16 = 0
q = (-1) * b / a / 2
ds = (b ** 2 - 4 * a * c) ** 0.5
ds1 = (b ** 2 - 4 * a * c)

if ds1 == 0:
    x1 = q
    ost = x1 % 1
    q3 = str(ost)
    ln = len(q3)
    if ost == 0:
        x1 = str(x1)
        q1 = x1.find('.')
        q2 = x1[0:q1]
        # ln == 3 and ost[3:4]==0:
        x1 = q2
    elif ost != 0 and ln <= 8:
        x1 = x1
    else:
        x1 = float('{0:.6f}'.format(x1))
        x1 = x1
    if str(x1) == '-0':
        x1 = '0'
    print(x1)

if ds1 > 0:
    x1 = q + ds / a / 2
    x2 = q - ds / a / 2
    ost1 = x1 % 1
    q13 = str(ost1)
    ln1 = len(q13)
    ost2 = x2 % 1
    q12 = str(ost2)
    ln2 = len(q12)

    if ost1 == 0:
        x1 = str(x1)
        q11 = x1.find('.')
        q12 = x1[0:q11]
        x1 = q12

    elif ost1 != 0 and ln1 <= 8:
        x1 = x1
    else:
        x1 = float('{0:.6f}'.format(x1))
        x1 = str(x1)

    if ost2 == 0:
        x2 = str(x2)
        q14 = x2.find('.')
        q15 = x2[0:q14]
        x2 = str(q15)

    elif ost2 != 0 and ln2 <= 8:
        x2 = str(x2)
    else:
        x2 = float('{0:.6f}'.format(x2))
        x2 = str(x2)

    if x1 <= x2:
        x1 = x1
    else:
        # q4 = x1
        # x1 = x2
        # x2 = q4
        (x1, x2) = (x2, x1)
        q16 = x2.find('.')
        if len(x2[q16 + 1:]) == 6:
            x2 = float(x2)
            x2 = float('{0:.5f}'.format(x2))
        print(x1, x2)
