numList = list(map(int, input().split()))
pList = []
negList = []
for q in range(len(numList)):
    if numList[q] > -1:
        pList.append(numList[q])
    else:
        negList.append(numList[q])
a2 = len(pList)
a3 = len(negList)
a4 = len(numList)
maxList = []
minList = []
nmaxList = []

s1 = 0
s2 = 0
s3 = 0

if a2 >= 1:
    max1 = pList[0]
    a1 = 0
    while a1 <= a2 - 1:
        if pList[a1] >= max1:
            max1 = pList[a1]
        a1 += 1
    s1 = 1
    maxList.append(max1)
    pList.remove(max1)
if a2 >= 2:
    max2 = pList[0]
    a1 = 0
    while a1 <= a2 - 2:
        if pList[a1] >= max2:
            max2 = pList[a1]
        a1 += 1
    s1 = 2
    maxList.append(max2)
    pList.remove(max2)
if a2 >= 3:
    max3 = pList[0]
    a1 = 0
    while a1 <= a2 - 3:
        if pList[a1] >= max3:
            max3 = pList[a1]
        a1 += 1
    s1 = 3
    maxList.append(max3)
if a3 >= 1:
    min1 = negList[0]
    a1 = 0
    while a1 <= a3 - 1:
        if negList[a1] <= min1:
            min1 = negList[a1]
        a1 += 1
    s2 = 1
    minList.append(min1)
    negList.remove(min1)
if a3 >= 2:
    min2 = negList[0]
    a1 = 0
    while a1 <= a3 - 2:
        if negList[a1] <= min2:
            min2 = negList[a1]
        a1 += 1
    s2 = 2
    minList.append(min2)
    negList.remove(min2)
if a3 >= 3 and s1 == 0:
    min3 = negList[0]
    a1 = 0
    while a1 <= a3 - 3:
        if negList[a1] <= min3:
            min3 = negList[a1]
        a1 += 1
    s2 = 3
    minList.append(min3)

if s1 == 0 and a3 > 1:
    nmax1 = numList[0]
    a1 = 0
    while a1 <= a4 - 1:
        if numList[a1] >= nmax1:
            nmax1 = numList[a1]
        a1 += 1
    s3 = 1
    nmaxList.append(nmax1)
    numList.remove(nmax1)

if s1 == 0 and a3 > 1:
    nmax2 = numList[0]
    a1 = 0
    while a1 <= a4 - 2:
        if numList[a1] >= nmax2:
            nmax2 = numList[a1]
        a1 += 1
    s3 = 2
    nmaxList.append(nmax2)
    numList.remove(nmax2)

if s1 == 0 and a3 > 1:
    nmax3 = numList[0]
    a1 = 0
    while a1 <= a4 - 3:
        if numList[a1] >= nmax3:
            nmax = numList[a1]
        a1 += 1
    s3 = 3
    nmaxList.append(nmax3)

if s1 + s2 < 3:
    print('')
elif s1 + s2 == 3 and s2 == 0:
    print(*maxList)
elif s1 + s2 == 3 and s1 != 0:
    print(*maxList, *minList, )
elif s1 + s2 == 3 and s1 == 0:
    print(*nmaxList)
elif s1 + s2 == 4 and s2 == 1:
    print(*maxList)
elif s1 + s2 == 4 and s2 > 1:
    print(maxList[0], minList[0], minList[1])
elif s1 + s2 >= 5:
    if max1 * max2 * max3 >= max1 * min1 * min2:
        print(max1, max2, max3)
    else:
        print(max1, min1, min2)
