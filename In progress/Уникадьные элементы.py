numList = list(map(int, input().split()))

countList = []
xList = []
a2 = len(numList)
x = 0
a3 = numList.count(x)
a1 = 0
a3 = 0

while a1 <= a2 - 1:
    a3 = numList.count(numList[a1])
    countList.append(a3)
    a1 += 1
a1 = 0
while a1 <= a2 - 1:
    if countList[a1] == 1:
        xList.append(numList[a1])
    a1 += 1

print(*xList)
