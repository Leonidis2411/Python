numList = list(map(int, input().split()))
q3 = len(numList)
q1 = 0
s = 0
while q1 <= q3 - 2:
    q2 = q1 + 1
    while q2 <= q3 - 1:
        if numList[q1] == numList[q2]:
            s += 1
        q2 += 1
    q1 += 1

print(s)
