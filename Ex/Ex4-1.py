
# counter = 0
# while counter < 3 :
#     print('yahoo')
#     counter= counter + 1
#
# for i in range(3):
#     print('yahoo2')
#
# ans = int(input('kazu'))
#
# counter = 0
# while counter < ans:
#     print(counter)
#     counter += 2
#
# for i in range(0,ans,2):
#     print(i)
#

# ans2 =int(input('A:'))
# ans3 =int(input('B'))
#
# ans2,ans3 = sorted([ans2,ans3])
#
# # for i in range(ans3,ans2,-1):
# #     print(i,end="")
# # print()
#
#
# while ans3 > ans2 :
#     print(ans3,end="")
#     ans3 = ans3 - 1
# print()

a4 = int(input('seisuu:'))

counter = 1
total = 0

while counter < a4:
    total += counter
    counter +=2
print(total)
total = 0
for i in range (1,a4,2):
    total += i
print()
print(total)
