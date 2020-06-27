def distance(x1, y1, x2, y2):
    dst = 0
    ost = 0
    ln = 0
    dst = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    ost = dst % 1
    ln = len(str(ost))
    if ost == 0:
        dst = int(dst)
    elif ost != 0 and 2 < ln <= 5:
        dst = dst
    elif ln > 5:
        dst = float('{0:.7f}'.format(dst))
    return dst


a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())
a6 = float(input())

l12 = 0
l13 = 0
l23 = 0
p = 0

x1 = a1
y1 = a2
x2 = a3
y2 = a4
l12 = distance(x1, y1, x2, y2)

x1 = a1
y1 = a2
x2 = a5
y2 = a6
l13 = distance(x1, y1, x2, y2)

x1 = a3
y1 = a4
x2 = a5
y2 = a6
l23 = distance(x1, y1, x2, y2)

p1 = l12 + l13 + l23
p = float('{0:.6f}'.format(p1))

print(p)
