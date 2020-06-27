def min4(a, b, c, d):
    f = 1
    f = min(min(a, b), min(c, d))
    return f


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
