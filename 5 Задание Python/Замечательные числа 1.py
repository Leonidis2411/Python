n = 35
s = ''
while n <= 96:
    n = n + 1
    if ((n // 10) * (n % 10)) * 2 == n:
        print(n)
