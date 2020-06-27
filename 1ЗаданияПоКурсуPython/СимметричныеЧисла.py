a = int(input())
a1 = a // 1000
a11 = a % 1000
a2 = a11 // 100
a12 = a11 % 100
a3 = a12 // 10
a4 = a12 % 10
b1 = (a1 - a4) ** 2
b2 = (a2 - a3) ** 2
c = (b1 + b2 + 3) // 2
print(str(c))
