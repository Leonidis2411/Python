n = int(input())
m = int(input())
k = int(input())
q1 = k % n
q2 = k // n
q3 = k % m
q4 = k // m
if q1 == 0 and q2 < m:
    print('YES')
else:
    if q3 == 0 and q4 < n:
        print('YES')
    else:
        print('NO')
