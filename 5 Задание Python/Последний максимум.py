numList = list(map(int, input().split()))
a1 = len(numList)
x = 0
s1 = numList[a1 - 1]
s2 = a1 - 1
while x <= a1 - 2:
    if numList[x] >= s1:
        s1 = numList[x]
        s2 = x
    x += 1
if s1 == numList[a1 - 1]:
    s2 = a1 - 1
print(s1, s2)
