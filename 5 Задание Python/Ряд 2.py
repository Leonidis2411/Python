a1 = int(input())
a2 = int(input())
if a1 < a2:
    for a2 in range(a1, a2 + 1):
        print(a2, end=" ")
else:
    for a2 in range(a1, a2 - 1, -1):
        print(a2, end=" ")
