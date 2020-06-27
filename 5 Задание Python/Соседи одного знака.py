numList = list(map(int, input().split()))
a1 = len(numList)
x = 1
s = ''
while x <= a1 - 1:
    if (numList[x - 1] * numList[x]) > 0:
        s = str(numList[x - 1]) + ' ' + str(numList[x])
        print(s)
        break
    x += 1
