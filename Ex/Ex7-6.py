import random

n = int(input('suu:'))

x = []
for i in range(n):
    r = random.randint(1, 10)
    x.append(r)
print(x)
s = int(input('search:'))
v = []

for i in range(n):
    if x[i] == s:
        v.append(i)


print(v)