q = int(input())
qMax = q
while q != 0:
    q = int(input())
    if q > qMax and q != 0:
        qMax = q
print(qMax)
