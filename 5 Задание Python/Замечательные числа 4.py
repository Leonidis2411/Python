a1 = int(input())
a2 = int(input())
if a1 > a2:
    a1, a2 = a2, a1
q2 = (a2 // 100) + 1
q1 = (a1 // 100)
q3 = 0
while q1 <= q2:
    if q1 % 10 == 0:
        q3 = q1 * 100 + q1 // 10
    else:
        q3 = q1 * 100 + (q1 % 10) * 10 + q1 // 10
    if q3 >= a1 and q3 <= a2:
        print(q3)
    q1 = q1 + 1
