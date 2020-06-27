x = int(input())
y = int(input())
a1 = y - x
n = 1
while a1 > 0:
    x = x + x * 0.1
    a1 = y - x
    n = n + 1
print(n)
