numList = list(map(int, input().split()))
pList =[]
negList = []
a4 = len(numList)
q = 0
while q <= a4-1:
    if numList[q] > -1:
        pList.append(numList[q])
    else:
        negList.append(numList[q])
print(*numList)
print(*pList)
print(*negList)


a2 = len(pList)
a3 = len(negList)

maxList = ['']
minList = ['']
s1 = 0
s2 = 0

if a2 >=1:
    max1 = pList[0]
    a1 = 0
    while a1 <= a2 - 1:
        if pList[a1] >= max1:
            max1 = pList[a1]
        a1 += 1
    s1 = 1
    maxList.append(max1)
    pList.remove(max1)

if a2 >=2:
    max3 = pList[0]
    a1 = 0
    while a1 <= a2 - 2:
        if pList[a1] >= max3:
            max3 = pList[a1]
        a1 += 1
    s1 = 3
    maxList.append(max3)

if a3 >=1:
    min1 = negList[0]
    a1 = 0
    while a1 <= a3 - 1:
        if negList[a1] >= min1:
            min1 = negList[a1]
        a1 += 1
    s2 = 1
    minList.append(min1)
    negList.remove(min1)

if a3 >=2:
    min2 = negList[0]
    a1 = 0
    while a1 <= a3 - 2:
        if negList[a1] >= min2:
            min2 = negList[a1]
        a1 += 1
    s2 = 2
    minList.append(min2)
    negList.remove(min2)

if a3 >=3 and s1 == 0:
    min3 = negList[0]
    a1 = 0
    while a1 <= a3 - 3:
        if negList[a1] >= min2:
            min3 = negList[a1]
        a1 += 1
    s2 = 3
    minList.append(min3)

if s1 + s2 < 3:
    print('')
elif s1 + s2 == 3:
    print(*maxList,*minList)

print(s1,s2)
print(*pList)
print(negList)


