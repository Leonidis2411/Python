a1 = input()
q = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q4 = a1.find('f')
if q4 != -1:
    q1 = a1.find('f')
    a2 = a1.replace('f', '0', 1)
    q2 = a2.find('f')

if q4 == -1:
    q = -2
elif q2 == -1:
    q = -1
elif q2 != -1:
    q = q2
print(q, )
