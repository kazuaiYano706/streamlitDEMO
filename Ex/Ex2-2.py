ans =int(input('tennsu'))

if ans >= 80:
    print('A')
elif ans >= 70:
    print('B')
elif ans >= 60:
    print('C')
else:
    print('D')

ans2 = int(input('1/3'))

if ans2 ==1 or ans2 == 3:
    print("1or3")
else:
    print('sonota')

ans3 = int(input('uruu'))

if ans3 %4 ==0 and ans3 %100 != 0 or ans3 %400 == 0:
    print('uruu')
else:
    print('not uruu')

ans4 = int(input('jouken'))
ans4 = print("guusuu") if ans4%2==0 else print("kisuu")

