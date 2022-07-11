# import random
#
#
# def hello():
#     print('hellow')
#
# hello()
#
# def lucky ():
#     num = random.randint(1,9)
#     print('your lucky number is',num)
#
# lucky()
# def draw_line(n):
#     for i in range(n):
#
#         if i%2 == 1:
#             print('-',end='')
#         else:
#             print('+', end='')
#
#
# n = int(input('times='))
#
# draw_line(n)

def std_weight(height):
    weight = (height- 100) * 0.9

    return weight


height = int(input('height:'))

weight = std_weight(height)

print(weight)

