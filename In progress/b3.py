numList = list(map(int, input().split()))
pList =[]
negList = []

for q in range(len(numList)):
    if numList[q] > -1:
        pList.append(numList[q])
    else:
        negList.append(numList[q])


#Test
a2 = len(pList)
a3 = len(negList)

maxList = []
minList = []
s1 = 0
s2 = 0

if a2 >=1
max1 = pList[0]
a1 = 0
while a1 <= a2 - 1:
    if pList[a1] >= max1:
        max1 = pList[a1]
    a1 += 1
s1 = 1
maxList.append(max1)

pList.remove(max1)






print(max1,len(maxList),*maxList)