x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 0:
    zx1 = 1
else:
    zx1 = -1
if y1 > 0:
    zy1 = 1
else:
    zy1 = -1
if x2 > 0:
    zx2 = 1
else:
    zx2 = -1
if y2 > 0:
    zy2 = 1
else:
    zy2 = -1
if zx1 == zx2 and zy1 == zy2:
    print('YES')
else:
    print('NO')
