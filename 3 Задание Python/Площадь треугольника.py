mMd1 = float(input())
mMd2 = float(input())
mMd3 = float(input())
s = 0
p = 0
if mMd1 >= mMd2 and mMd1 >= mMd3:
    a3 = mMd1
if mMd2 >= mMd1 and mMd2 >= mMd3:
    a3 = mMd2
if mMd3 >= mMd1 and mMd3 >= mMd2:
    a3 = mMd3

if mMd1 <= mMd2 and mMd1 <= mMd3:
    a1 = mMd1
if mMd2 <= mMd1 and mMd2 <= mMd3:
    a1 = mMd2
if mMd3 <= mMd1 and mMd3 <= mMd2:
    a1 = mMd3
if (mMd1 - mMd2) * (mMd1 - mMd3) <= 0:
    a2 = mMd1
if (mMd2 - mMd1) * (mMd2 - mMd3) <= 0:
    a2 = mMd2
if (mMd3 - mMd1) * (mMd3 - mMd2) <= 0:
    a2 = mMd3
a1 = a1 // 1
if (a1 + a2) > a3:
    p = (a1 + a2 + a3) / 2
    s = abs(p * (p - a1) * (p - a2) * (p - a3)) ** 0.5
if s % 1 == 0:
    s = int(s)
else:
    s = '{0:.6f}'.format(s)
print(s)
