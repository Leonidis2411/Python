n = int(input())
s1 = ('+' + '_' * 3 + ' ') * n
s2 = '|' + '&' + ' ' + '/' + ' '
s2 = s2 * n
q = 1
while q <= n:
    s2 = s2.replace('&', str(q), 1)
    q += 1
s3 = ('|' + '_' + '_' + '\\' + ' ') * n
s4 = ('|' + ' ' * 4) * n
print(s1)
print(s2)
print(s3)
print(s4)
