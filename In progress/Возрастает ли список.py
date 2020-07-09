def isEven(n):
    return n % 2 == 0


def isAssending(A):
    q2 = len(A)
    q1 = 1
    s = 1
    while q1 <= q2 - 1:
        if A[q1] > A[q1 - 1]:
            s += 1
        q1 += 1
    return (q2) == s


A = list(map(int, input().split()))
if isAssending(A):
    print('YES')
else:
    print('NO')
