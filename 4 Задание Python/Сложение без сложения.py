def sum(a, b):
    if b == 0:
        return a
    return (sum(a, b - 1) + 1)


a = int(input())
b = int(input())
c = sum(a, b)

print(c)
