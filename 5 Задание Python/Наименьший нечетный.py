numList = list(map(int, input().split()))
a1 = len(numList)
x = 0
s2 = 0
s1 = 0
while x <= a1 - 1:
    if (numList[x]) % 2 != 0:
        s1 = numList[x]
        s2 = x
        break
    x += 1
x = s2
while x <= a1 - 1:
    if numList[x] % 2 != 0 and numList[x] < s1:
        s1 = numList[x]
    x += 1

print(s1)
