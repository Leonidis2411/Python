numList = list(map(int, input().split()))
a1 = len(numList)
x = 1
s1 = ''
s2 = 0
while x <= a1 - 1:
    if numList[x] > numList[x - 1]:
        s1 = s1 + str(numList[x]) + ' '
    x += 1
print(s1)
