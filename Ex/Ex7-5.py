str = 'ABC,DEF,GHI,JKL'

lst = str.split(',')

for i, name in enumerate(lst):
    print(f'lst[{i}]={name}')

x = []
while True:
    a = int(input('No:'))
    if a <= 0 :
        break
    else:
        for i in range(len(x)):
            if a == x[i]:
                print('alredy exist')
                break
        else:
            x.append(a)
print(x)
