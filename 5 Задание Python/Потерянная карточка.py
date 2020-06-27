n = int(input())
q1 = 1
s = 0
while q1 <= n - 1:
    a = int(input())
    s += a
    q1 = q1 + 1
s1 = (1 + n) * (n / 2)
print(int(s1 - s))
