a1 = input()
a4 = 0
a2 = a1.find('.')
a3 = a1[a2 + 1:]
if float(a1) > 0 and int(a3) > 4:
    a4 = int(float((a1))) + 1
elif float(a1) > 0 and int(a3) < 5:
    a4 = int(float((a1)))
elif float(a1) < 0 and int(a3) < 6:
    a4 = int(float((a1)))
elif float(a1) < 0 and int(a3) > 5:
    a4 = int(float((a1))) - 1


print(a4)
