def max2(a,b):
    max = a
    if max < b:
        max = b
    return max

n1 = int(input('整数n1：'))
n2 = int(input('整数n2：'))

print('最大値は',max2(n1,n2),'です。')

