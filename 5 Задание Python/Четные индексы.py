numList = list(map(int, input().split()))
a1 = len(numList)
x = 0
while x <= (a1 if a1 % 2 != 0 else a1 - 1):
    print(numList[x], end=' ')
    x += 2
