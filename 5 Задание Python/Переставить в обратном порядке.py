numList = list(map(int, input().split()))
a1 = len(numList)
x = 0
s2 = 0
s1 = 0
numList1 = [0] * a1
x = 0
while x <= a1 - 1:
    numList1[a1 - 1 - x] = numList[x]
    x += 1


x = 0
while x <= a1 - 1:
    numList[x] = numList1[x]
    x += 1
x = 0
while x <= a1 - 1:
    print(numList[x], end=' ')
    x += 1
