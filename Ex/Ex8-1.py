lst1 = [12,11,31]
lst2 = [26,14,12]

lst= tuple(zip(lst1,lst2))
print(lst)
for i ,j, in enumerate(lst):
    a,b = j
    print(a,b,a+b)

