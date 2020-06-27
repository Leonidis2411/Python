q = input()
q1 = 0
s = 0
ln = 0
q2 = 0

q1 = q.find('.')
if float(q) < 1:
    s = q
elif q1 != -1:
    q2 = q[(q1 + 1):]
    s = '0' + '.' + q2

print(s)
