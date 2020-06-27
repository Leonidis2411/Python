a1 = input()
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0
q1 = a1.find(' ')
q2 = ' ' + a1[0:q1]
q5 = a1[0:q1 + 1]
q3 = a1 + q2
q4 = q3.replace(q5, '', 1)
print(q4)
