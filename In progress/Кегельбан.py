NkList = list(map(int, input().split()))
N = NkList[0]
k = NkList[1]
strikeList = []
q = 0
while q <= k - 1:
    numList = list(map(int, input().split()))
    strikeList.extend(numList)
    q += 1
Ilist = ['I'] * N
kList = []
q = 1
s = 0
while q <= k:
    s = strikeList[q * 2 - 1]
    q1 = strikeList[q * 2 - 2]
    while q1 <= s:
        kList.append(q1)
        q1 += 1
    q += 1

q1 = 0
while q1 < len(kList):
    Ilist.insert(kList[q1] - 1, '.')
    Ilist.pop(kList[q1])
    q1 += 1

print(*Ilist, sep='')
