numList = list(map(int, input().split()))
a1 = len(numList)
x = 1
s1 = 0

while x <= a1 - 2:
    if numList[x + 1] < numList[x] > numList[x - 1]:
        s1 = s1 + 1
    x += 1
print(s1)
