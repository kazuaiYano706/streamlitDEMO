import random
#
# a = random.randint(1,6)
# b = random.randint(1,6)
# ans = a+b
# print(a,b,"=")
#
# if ans %2 == 0 :
#     print('gousuu')
# else:
#     print('kiss')
# ans = 0
# while True:
#     a = random.randint(1,6)
#     ans += a
#     print(a,'=====',ans)
#     if ans > 20 :
#         break
#
# a = int(input('A:'))
# n = int(input('N:'))
# print(a,'made',n,'kai')
#
# for i in range(n):
#     for j in range(a):
#         print(j,end='')
#     print()
tan = int (input('tan='))
counter = 0
counter2 = tan

i = 0
while i < tan :
    while counter < tan:
        print ('*',end="")
        counter +=1
    while counter2 >tan:
        print('*',end='')
        counter2 -= 1
    print()
    i += 1

