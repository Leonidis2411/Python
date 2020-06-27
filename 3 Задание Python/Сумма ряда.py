n = int(input())
q = 1
s = 0
ost = 0
ln = 0
s = float('{0:.5f}'.format(s))
while q <= n:
    s = s + 1 / q ** 2
    q = q + 1
ost = s % 1
ost = str(ost)
ln = len(ost)
if ln <= 7:
    s = s
else:
    s = float('{0:.5f}'.format(s))
print(s, )
