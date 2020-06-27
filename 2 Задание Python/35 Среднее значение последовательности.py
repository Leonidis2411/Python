q = int(input())
q1 = 0
sum = 0
while q != 0:
    q1 = abs(q % 2)
    sum = sum + abs(q / q) - q1
    q = int(input())
print(sum)
