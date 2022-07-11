import random

# x = []
# while True :
#     a = int(input('How many?'))
#     if 1 <= a <= 9:
#         break
#
# for _ in range(a):
#     while True:
#         v = random.randint(1,10)
#         if v not in x:
#             break
#
#     x.append(v)
# print(x)

keta = 4
times = 150
kaygyou = 15
b = []

for j in range(1,times+1):
    for _ in range(keta):
        while True:
            a = random.randint(0, 9)
            if a not in b:
                break
        b.append(a)
    for i in range(keta):
        print(b[i], end='')
    print(' ', end='')
    del b[:]
    if j % kaygyou == 0:
        print()
