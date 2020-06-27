def xor(x, y):
    s = x + y
    if s == 0 or s == 2:
        s = 0
    else:
        s = 1
    return s


x = int(input())
y = int(input())
print(xor(x, y))
