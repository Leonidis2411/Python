q1 = int(input())
k = 0
q2 = 1
while q2 <= q1:
    q2 = q2 * 2
    if q1 == 1:
        k = 0
    elif q1 == 2:
        k = 1
    elif q2 == q1:
        k = k + 0
    else:
        k = k + 1
print(str(k))
