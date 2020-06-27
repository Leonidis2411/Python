a, b, c = str(input()), str(input()), str(input())
d, e = str(input()), str(input())
if int(b) < int(a):
    (a, b, c) = (b, a, c)
if int(b) > int(c):
    (a, b, c) = (a, c, b)
if int(b) < int(a):
    (a, b, c) = (b, a, c)
if int(d) > int(e):
    (d, e) = (e, d)
if int(d) >= int(a) and int(e) >= int(b):
    print('YES')
else:
    print('NO')
