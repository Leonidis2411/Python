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
        dst = float('{0:.5f}'.format(dst))
    return dst


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance(x1, y1, x2, y2))
