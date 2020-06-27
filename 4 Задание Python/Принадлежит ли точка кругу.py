def IsPointInCircle(x, y, xc, yc, r):
    a = abs(((x - xc) ** 2 + (y - yc) ** 2) ** 0.5)
    return a <= r


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())

if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
