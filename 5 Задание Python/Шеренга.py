# numList = [165,163,160,160,157,157,155,154]
numList = list(map(int, input().split()))
x = int(input())
numList.append(0)
a2 = len(numList)
# print(a2)
s1 = 0
a1 = 0
while a1 <= a2 - 2:
    if x > numList[0]:
        s1 = 1
    elif x <= numList[a1] and x > numList[a1 + 1]:
        s1 = a1 + 2
    a1 += 1
print(s1)
