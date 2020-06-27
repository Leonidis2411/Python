ye = int(input())
div1 = 4
div2 = 100
div3 = 400
q1 = ye % div1
q2 = ye % div2
q3 = ye % div3
if q3 == 0:
    print('Yes')
else:
    if q2 == 0:
        print('No')
    else:
        if q1 == 0:
            print('Yes')
        else:
            print('No')
