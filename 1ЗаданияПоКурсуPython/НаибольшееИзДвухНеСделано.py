A = int(input())
B = int(input())
a1 = B//A
a2 = B%A
a3 = A//B
a4 = A%B
z=a1+a3
zy = a1*a2+a3*a4
y = zy // z
xy = a2+a4
x = xy-y
M = z*x+y
print(str(a1),str(a2),str(a3),str(a4),str(z),str(x),str(y),str(M))
print(str(M))




