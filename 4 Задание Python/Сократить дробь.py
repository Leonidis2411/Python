import math
def zn(n):
    zn = math.signe(n)-1
    return zn


a = float(input())
b = float(input())
c = float(input())
xt = float(input())

yt = float(input())

a1 = 1
b1 = 1
c1 = 0
a2 = 2
b2 = -1
c2 = 2
xc = -1
yc = 1
r = 2
s1 = 0
s2 = 0
dst = 0
yp = 2/3


s1 = a1 * xt + b1 * yt + c1
s2 = a2 * xt + b2 * yt + c2
dst = ((xt-xc)**2 + (yt - yc)**2)**0.5

#if yt >= yp:
print(zn(a) ,zn(b) ,zn(c))