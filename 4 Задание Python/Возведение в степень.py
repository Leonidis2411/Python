def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


a = float(input())
n = int(input())
rez = power(a, n)
if rez % 1 == 0:
    rez = int(rez)
else:
    rez = rez
print(rez)
