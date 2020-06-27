def viv(rez):
    if rez % 1 == 0:
        return int(rez)
    else:
        return rez


a = float(input())
n = int(input())
if n == 0:
    a = 1
elif n % 2 == 0:
    a = (a ** 2) ** (n / 2)
    a = viv(a)
else:
    a = a * (a ** 2) ** ((n - 1) / 2)
    a = viv(a)
print(a)
