a1 = input()
a2 = a1.find('h')
a3 = a1.rfind('h')
a4 = a1[a2:a3 + 1]
a5 = a1.replace(a4, '')
print(a5, )
