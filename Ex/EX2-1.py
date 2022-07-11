ans = int(input('tensuu'))

if ans >=50:
    print('合格')
else:
    print('不合格')

ans2 = int(input('sannsei'))

if ans2==1 :
    print('賛成')
else:
    print('反対')

ans3 = int(input('kisuu'))

if ans3 % 2 == 0:
    print('偶数')
else:
    print('奇数')

ans4 = int(input('dantai'))
enter = 850
discount = 0.3

if ans4 >= 5:
    print(ans4*enter * discount)
else:
    print(ans4*enter)




