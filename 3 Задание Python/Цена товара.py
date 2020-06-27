q = input()
q1 = 0
rb = 0
kp = 0

q1 = q.find('.')
rb = int(q[0:(q1)])
kp = int(q[(q1 + 1):])

print(rb, kp)
