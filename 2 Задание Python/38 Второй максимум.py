q = int(input())
qMax1 = 0
qMax2 = 0
qMax3 = 0
qMax = 0
n = 0
q1 = 1
while q != 0:
    q = int(input())
    n = n + 1
    if q >= qMax1:
        qMax2 = qMax1
        qMax1 = q
        qMax = qMax2
        continue
    if n == 2:
        if qMax2 == 0:
            qMax = qMax1
    else:
        qMax = qMax2
print(qMax)
print(qMax1, qMax2)
