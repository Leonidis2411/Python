numList = list(map(int, input().split()))
a2 = len(numList)
s1 = numList[0]
s2 = numList[0]
s3 = 0
s4 = 0

a1 = 0
while a1 <= a2 - 1:
    if numList[a1] >= s1:
        s1 = numList[a1]
        s3 = a1
    elif numList[a1] <= s2:
        s2 = numList[a1]
        s4 = a1
    a1 += 1
numList[s3] = s2
numList[s4] = s1
print(*numList)
