numList = list(map(int, input().split()))
a1 = len(numList)
x = 0
s = 0
while x <= a1 - 1:
    if numList[x] > 0:
        s += 1
    x += 1
print(s)
