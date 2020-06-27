n = int(input())
n1 = n // 10
n2 = n % 10
if n2 == 1 and n1 != 1:
    print(str(n), 'korova', sep=' ')
elif 1 < n2 < 5 and n1 != 1:
    print(str(n), 'korovy', sep=' ')
else:
    print(str(n), 'korov', sep=' ')
