def IsPointInSquare(x, y):
    a = max(abs(x), abs(y))
    return a <= 1


x = float(input())
y = float(input())

if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
