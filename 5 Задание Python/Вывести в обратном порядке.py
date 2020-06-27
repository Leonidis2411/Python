numList = list(map(int, input().split()))
a1 = len(numList)
x = 0
s2 = 0
s1 = 0
x = a1 - 1

while x >= 0:
    print(numList[x], end=' ')
    x -= 1