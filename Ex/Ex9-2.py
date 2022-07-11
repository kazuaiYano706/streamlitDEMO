# a = 10
# b = 15
#
# add = lambda x,y: x+y
#
# print (add(a,b))
#
# print((lambda x, y: x * y)(a,b))
#
#
# x = [1,2,3,4,5,6,]
#
# y= map(lambda n: 2*n,x)
# print(x)
# print(y)
# print(tuple(y))
# print(list(y))


import random

number = int(input('How many student?:'))

point = [None] * number

for i in range(number):
    point[i] = random.randint(0,100)
print(point)
print('clear:',list(filter(lambda n:n>=80,point)))


