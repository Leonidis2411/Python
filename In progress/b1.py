numList = list(map(int, input().split()))



pList =[]
negList = []

for q in range(len(numList)):
    if numList[q] > -1:
        pList.append(numList[q])
    else:
        negList.append(numList[q])



a2 = len(pList)
a3 = len(negList)


if (a2 + a3) < 3:
    print('')
elif a2 == 0 and (a2 + a3) == 3:
    print(negList[0],negList[1],negList[2],)
elif  a2 == 1 and (a2 + a3) == 3:
    print(negList[0],negList[1],pList[0],)
elif  a2 == 2 and (a2 + a3) == 3:
    print(negList[0],pList[1],pList[0],)
elif  a2 == 3 and (a2 + a3) == 3 or (a2 + a3) == 4:
    print(pList[2],pList[1],pList[0],)
elif a2>3 and a3 <2:
    max1 = pList[0]
    a1 = 0
    while a1 <= a2 - 1:
        if pList[a1] >= max1:
            max1 = pList[a1]
        a1 += 1
    pList.remove(max1)

    max2 = pList[0]
    a1 = 0
    while a1 <= a2 - 2:
        if pList[a1] >= max2:
            max2 = pList[a1]
        a1 += 1
    pList.remove(max2)

    max3 = pList[0]
    a1 = 0
    while a1 <= a2 - 3:
        if pList[a1] >= max3:
            max3 = pList[a1]
        a1 += 1
    print(max1,max2,max3)
elif  a2>3 and a3 <2:
    a4 = len(numList)
    max1 = numList[0]
    min1 = numList[0]
    a1 = 0
    while a1 <= a4 - 1:
        if numList[a1] >= max1:
            max1 = numList[a1]
        if numList[a1] <= min1:
            min1 = numList[a1]
        a1 += 1
    pList.remove(max1)
    negList.remove(min1)

    max2 = pList[0]


    a1 = 0
    while a1 <= a2 - 2:
        if pList[a1] >= max2:
            max2 = pList[a1]
        a1 += 1
    pList.remove(max2)

    max3 = pList[0]
    a1 = 0
    while a1 <= a2 - 3:
        if pList[a1] >= max3:
            max3 = pList[a1]
        a1 += 1

    min2 = negList[0]
    a1 = 0
    while a1 <= a3 - 2:
        if negList[a1] <= min2:
            min2 = pList[a1]
        a1 += 1

    if max1*max2*max3 >= max1 * min1 * min2:
        print(max1,max2,max3)
    else:
        print(max1, min1, min2)




