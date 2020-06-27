numList = list(map(int, input().split()))
a1 = len(numList)
x = 0
s1 = 1000
s2 = 0
while x <= a1 - 1:
    if numList[x] <= 0:
        s1 = s1 + 0
    elif numList[x] <= s1:
        s1 = numList[x]
    x += 1

print(s1)
