n = int(input())
numList = list(map(int, input().split()))
x = int(input())
numList1 = [0] * n

a1 = 0
while a1 <= n - 1:
    numList1[a1] = abs(x - numList[a1])
    a1 += 1
s = numList1[0]

s1 = 0
a1 = 0
while a1 <= n - 1:
    if numList1[a1] < s:
        s1 = a1
        s = numList1[a1]
    a1 += 1

print(numList[s1])
