numList = list(map(int, input().split()))
a2 = len(numList)
max1 = numList[0]
min1 = numList[0]
inmax1 = 0
inmin1 = 0

a1 = 0
while a1 <= a2 - 1:
    if numList[a1] >= max1:
        max1 = numList[a1]
        inmax1 = a1
    if numList[a1] <= min1:
        min1 = numList[a1]
        inmin1 = a1
    a1 += 1
max1 = numList.pop(inmax1)
if inmin1 > inmax1:
    min1 = numList.pop((inmin1 - 1))
else:
    min1 = numList.pop(inmin1)

max2 = numList[0]
min2 = numList[0]
inmax2 = 0
inmin2 = 0
a1 = 0
while a1 <= a2 - 3:
    if numList[a1] >= max2:
        max2 = numList[a1]
        inmax2 = a1
    if numList[a1] <= min2:
        min2 = numList[a1]
        inmin2 = a1
    a1 += 1
max2 = numList.pop(inmax2)
if inmin2 > inmax2:
    min2 = numList.pop((inmin2 - 1))
else:
    min2 = numList.pop(inmin2)

if max1 * max2 >= min1 * min2:
    print(max2, max1)
else:
    print(min1, min2)
