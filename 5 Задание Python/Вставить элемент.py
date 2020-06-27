numList = list(map(int, input().split()))
numList1 = list(map(int, input().split()))
a1 = len(numList)
numList.append(0)
numList2 = numList[numList1[0]:a1]
numList[numList1[0] + 1:a1 + 1] = numList2
numList[numList1[0]] = numList1[1]
x = 0
while x <= a1:
    print(numList[x], end=' ')
    x += 1