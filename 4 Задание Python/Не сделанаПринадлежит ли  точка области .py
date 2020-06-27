import math
def pi():
    return math.atan2(1, 0)*2


def dirang(xt,yt,xp,yp):
    dx = xt - xp
    dy = yt - yp
    q = math.atan2(dy, dx)
    if q >= 0:
        return q
    else:
        return q + 2 * float(pi())


def dst(xt, yt, xc, yc):
    dst = ((xt-xc)**2 + (yt-yc)**2)**0.5
    return dst



def rad():
    return 180 / pi()



xt = float(input())
yt = float(input())
xp = -2/3
yp = 2/3
xc = -1
yc = 1

dst = dst(xt, yt, xc, yc)
dir1 = dirang(0,2,xp,yp)
dir2 = dirang(-1,1,xp,yp)
dirt = dirang(xt,yt,xp,yp)
if dst > 2 and (dir1 + float(pi()))>dirt>=0:
    print('NO')
elif dst > 2 and float(pi()*2)>dirt>dir2+float(pi()):
    print('NO')
elif dst < 2 and float(2*pi())>=dirt>dir2:
    print('NO')
elif dst < 2 and 0<=dirt<dir1:
    print('NO')
else:
    print('YES')
print('dir1 = ',dir1*rad())
print('dir2 = ',dir2*rad())
print('dirt = ',dirt*rad())
print('dst= ',dst)


