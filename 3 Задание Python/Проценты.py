p = int(input())
rb = int(input())
kp = int(input())
pr = 0
s = 0
s = (rb * 100 + kp)
pr = (s * p) // 100
s = s + pr
rb = s // 100
kp = s % 100
print(rb, kp)
