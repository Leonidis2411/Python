a1 = input()
a2 = a1.find('h')
a3 = a1.rfind('h')
a4 = a1[a2 + 1:a3]
a5 = a1[0:a3]
a6 = a1[a3:]
a7 = a5 + a4 + a6

print(a7, )
