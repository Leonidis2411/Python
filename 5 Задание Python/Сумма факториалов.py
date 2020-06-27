n = int(input())
s = 0
a = 1
k = 1
while k <= n:
    a = a * k
    s += a
    k = k + 1
print(s)
