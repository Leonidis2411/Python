n = int(input())
n1 = 10 ** n

for x in range(n1 - 1, -1 if n == 1 else (10 ** (n - 1)) - 1, -2):
    print(x, end=' ')
