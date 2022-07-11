# n = int(input('No.:'))
#
# lst = [3, 5, 8, 1, 6]
# lst2 = []
#
# for i in range(len(lst)):
#     lst2.append(lst[i]*n)
#
# print(lst2)

# lst = [1.5,2.3,0.6,3.3,9.0]
#
# for i in range(len(lst)):
#     print(lst[i])
# print('--------------------------------------------')
# for i in range(lst.index(lst[-1])+1):
#     print(lst[i])

# lst1 = [12, 11, 31]
# lst2 = [26, 14, 12]
# new_lst =[]
# for i in range(len(lst1)):
#     new_lst.append(lst1[i]+lst2[i])
# print(new_lst)

lst = [10,20,30,40,50,60]
v = len(lst)

for i in range(v-1,-1,-1):
    print(lst[i],end='\t')
