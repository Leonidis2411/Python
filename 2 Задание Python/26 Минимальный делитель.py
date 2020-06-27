q1 = int(input())
q2 = 2
while q2 <= q1:
    if (q1 % q2 == 0):
        # a1 = q2
        print(str(q2))
        break
    q2 = q2 + 1
