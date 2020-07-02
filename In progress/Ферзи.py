xyList = []
q = 0
while q <= 7:
    numList = list(map(int, input().split()))
    xyList.extend(numList)
    q += 1
s = 0
q1 = 0

while q1 <= 13:
    q2 = q1 + 2
    while q2 <= 15:
        dx = xyList[q2] - xyList[q1]
        dy = xyList[q2 + 1] - xyList[q1 + 1]
        if dx == 0 or dy == 0 or abs(dy / dx) == 1:
            s += 1
            break
        q2 += 2
    if s != 0:
        break
    q1 += 2

print('NO' if s == 0 else 'YES')
