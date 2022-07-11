import random

# y = int(input('youso:'))
#
# x = []
#
# for i in range(y):
#     x.append(random.randint(0, 9))
# print(x)
#
# s = int(input('sakujo:'))
#
# if s in x:
#     x.remove(s)
#     print(x)
# else:
#     print('not exist')
#


y = int(input('youso:'))

x = []

for i in range(y):
    x.append(random.randint(0, 9))
print(x)

s = int(input('sakujo:'))

while True :
    if s in x :
        x.remove(s)
    elif s not in x:
        break
print(x)

