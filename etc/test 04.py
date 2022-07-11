def sum_1ton(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x= int(input('ｘの値：'))
total = sum_1ton(x)
print(f'１から{x}までの和は{total}です')
