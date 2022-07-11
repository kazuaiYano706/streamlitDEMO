# hands = ['goo','choki','paa']
#
# a = int(input('input your hand-number:'))
#
# if 0 <= a <= 2:
#     print(hands[a])
# else:
#     print('your hand-number is not cool.')

season = []

for _ in range (2):
    season.append('冬')
for _ in range (3):
    season.append('春')
for _ in range (3):
    season.append('夏')
for _ in range (3):
    season.append('秋')
season.append('冬')

a = int(input('month'))

if 0 < a < 13:
    print(season[a])
else:
    print('erroe')

