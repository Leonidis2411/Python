def phib(n):
    if n == 0 or n == 1:
        return (n)
    else:
        return phib(n - 2) + phib(n - 1)


n = int(input())
print(phib(n))
