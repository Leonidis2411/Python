# numList = [165,163,160,160,157,157,155,154]
numList = list(map(int, input().split()))
a2 = len(numList)
s1 = 0
a1 = 0
while a1 <= a2 - 2:
    if numList[a1] != numList[a1 + 1]:
        s1 += 1
    a1 += 1
s1 = s1 + 1
print(s1)
