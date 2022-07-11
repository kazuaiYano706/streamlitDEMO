def put_star(n):
    for _ in range(n):
       print('*',end='')

print('長方形')
h = int(input('高さ：'))
w = int(input('横幅：'))

for i in range(1,h+1):
    put_star(w)
    print()

    
