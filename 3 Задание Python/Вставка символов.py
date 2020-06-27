a1 = input()
q1 = 0
q3 = ''
q4 = ''
n = 1
# q1 = a1.replace('1', 'one')
# q1 = a1.replace('1', 'one')
q1 = len(a1)
# a1 = a1 + ' '
q2 = '*'
while n <= q1:
    q3 = q2 + a1[n - 1:n]
    q4 = q4 + q3
    n = n + 1
q4 = q4.replace('*', '', 1)
print(q4)
