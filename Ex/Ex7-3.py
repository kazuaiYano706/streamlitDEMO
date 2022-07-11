import datetime

y = int(input('year:'))
m = int(input('month:'))
dm = m + 1
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 01,02,03,04,05,06,07,08,09,10,11,12
aaaa = ['月', '火', '水', '木', '金', '土', '日']

if not (1 <= m <= 12):
    print('eeroe')

elif m == 2:
    if y % 4 == 0 or y % 100 != 0 and y % 400 == 0:
        d2 = 29
        aaa = datetime.date(y, m, d2)
        nu = aaa.weekday()
        print(f'{y}年{m}月{d2}日（{aaaa[nu]}）')
    else:
        aaa = datetime.date(y, m, d[dm])
        nu = aaa.weekday()

        print(f'{y}年{m}月{d[dm]}日（{aaaa[nu]}）')
else:
    aaa = datetime.date(y, m, d[dm])
    nu = aaa.weekday()
    print(f'{y}年{m}月{d[dm]}日（{aaaa[nu]}）')
