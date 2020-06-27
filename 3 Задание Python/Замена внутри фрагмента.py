a1 = input()
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0
q6 = 0
q2 = a1.find('h')
q3 = a1.rfind('h')
q4 = a1[q2 + 1:q3]
q5 = q4.replace('h', 'H')
q6 = a1.replace(q4, q5)
print(q6)
