numList = list(map(int, input().split()))
regList = []
s = 0
for q in range(len(numList)):
    if numList[q] == 0:
        regList.append(numList[q])
    else:
        regList.insert(s, numList[q])
        s += 1

print(*regList)
