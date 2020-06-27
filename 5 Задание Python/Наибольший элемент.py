numList = list(map(int, input().split()))
a1 = len(numList)
x = 1
s1 = numList[0]
s2 = 0
while x <= a1 - 1:
    if numList[x] > s1:
        s1 = numList[x]
        s2 = x
    x += 1
if s1 == numList[0]:
    s2 = 0
print(s1, s2)
