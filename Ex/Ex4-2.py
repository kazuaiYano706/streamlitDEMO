# counter = 1
#
# while counter< 21:
#     print('2**',counter,'=',2**counter)
#     counter += 1
# print('--------------------------')
# for i in range(1,21):
#     print('2**',i,'=',2**i)

# a1 = int(input('gassan:'))
# ctr = 2
# total = 0
# printer = ""
#
# while ctr < a1+1:
#     printer = printer +'+' + str(ctr)
#     total += ctr
#     ctr += 1
# print('1'+printer,'=',total)
#
# total = 0
# times = 0
# while True :
#     s = int (input('seisuu:'))
#     if s <=0:
#         break
#     else:
#         times += 1
#         total += s
#         print('input',s)
# print('total=',total,'ave=',total/times)

# while True :
#     hand = int(input('hand='))
#     if 0 <= hand <3:
#         break
# print("your hand is ",end='')
# if hand == 0:
#     print('goo')
# elif hand ==1:
#     print('choki')
# else:
#     print('paa')

# a = int(input('mojisuu:'))
#
# moji = ""
# counter =0
# while counter < a:
#     if counter %2 ==0:
#         moji += "+"
#     else:
#         moji += "-"
#     counter += 1
# print(moji)

a = int(input('hyouji:'))
counter = 1

while counter < a+1 :
    if counter == 0:
        print("+",end="")
    elif counter%5 == 0:
        print("+")
    else :
        print("+",end="")
    counter += 1

