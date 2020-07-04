numList = list(map(int, input().split()))
a1 = len(numList)

s1 = 0
s2 = 0
q1 = 0
while q1 <= a1 - 1:
    if numList.count(numList[q1]) > s1:
        s1 = numList.count(numList[q1])
        s2 = q1
    q1 += 1
print(numList[s2])
