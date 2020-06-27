numList = list(map(int, input().split()))
a1 = len(numList)
x = 0
while x <= a1 - 1:
    if numList[x] % 2 == 0:
        print(numList[x], end=' ')
    x += 1
