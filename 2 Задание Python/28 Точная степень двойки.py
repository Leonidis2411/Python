q1 = int(input())
q2 = 2
a3 = 'YES'
while q2 <= q1:
    a1 = q1 // q2
    a2 = q1 % q2
    if q1 == 1:
        a3 = 'YES'

    elif a2 == 0 and a1 < 2:
        a3 = 'YES'
    else:
        a3 = 'NO'
    q2 = q2 * 2

print(a3)
