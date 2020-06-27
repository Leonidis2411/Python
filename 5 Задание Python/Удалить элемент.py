numList = list(map(int, input().split()))
k = int(input())
a2 = numList.pop(k)
a1 = len(numList)
x = 0
while x <= a1 - 1:
    print(numList[x], end=' ')
    x += 1
