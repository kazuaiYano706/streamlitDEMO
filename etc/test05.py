def max3(a,b,c):
    max = a
    if b > max: max= b
    if c > max: max= c
    return max

n1 = int(input('整数　n1 :'))
n2 = int(input('整数　n2 :'))
n3 = int(input('整数　n3 :'))
max = max3(n1,n2,n3)
print(f'最大値は{max}です')