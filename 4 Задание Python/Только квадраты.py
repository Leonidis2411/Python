s1 = ''
s = ''
n = -1
while n != 0:
    n = int(input())
    if n == 0:
        s = s
    elif (n ** 0.5 % 1) == 0:
        s = s + ',' + str(n)

k = s.rfind(',')
if s == '':
    s1 = 0
elif len(s) == 2:
    s1 = s[1]
else:
    while k != 0:
        k = s.rfind(',')
        s1 = s1 + ' ' + s[k + 1::]
        s = s.replace(s[k::], '')

print(s1)
