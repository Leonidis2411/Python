a1 = input()
a2 = a1.find('f')
a3 = a1.rfind('f')
if a2 == a3 == -1:
    a2 = ''
    a3 = ''
elif a2 == a3:
    a3 = ''

print(a2, a3)
