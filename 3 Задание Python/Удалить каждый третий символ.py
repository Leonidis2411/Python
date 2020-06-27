a1 = input()
q1 = 0
q3 = ''
q4 = ''
q5 = 0
cel = 0
ost = 0
n = 0
# q1 = a1.replace('1', 'one')
# q1 = a1.replace('1', 'one')
q1 = len(a1)
cel = q1 // 3
ost = q1 % 3

while n <= 3 * cel - 1:
    n = n + 3
    q3 = a1[n - 2:n]
    q4 = q4 + q3

q5 = a1[3 * cel + 3 - ost:]
q4 = q4 + q5
print(q4)
