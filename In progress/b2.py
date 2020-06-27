def sumkv():
    n = float(input())
    if n**0.5 == 0:
        return 0
    return n + sumkv()



s = '0'
print(sumkv())
