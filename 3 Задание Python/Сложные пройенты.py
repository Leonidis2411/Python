p = int(input())
rb = int(input())
kp = int(input())
kl = int(input())
q = 1
pr = 0
s = 0
while q <= kl:
    s = (rb * 100 + kp)
    pr = (s * p) // 100
    s = s + pr
    rb = s // 100
    kp = s % 100
    q = q + 1
print(rb, kp)
