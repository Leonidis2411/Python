a, b, c = str(input()), str(input()), str(input())
(a, b, c) = (b, a, c)
if int(b) < int(a):
    (a, b, c) = (b, a, c)
if int(b) > int(c):
    (a, b, c) = (a, c, b)
if int(b) < int(a):
    (a, b, c) = (b, a, c)
print(a, b, c)
