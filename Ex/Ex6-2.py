str = input('str?:')
sub = input('sub?:')
head = str.find(sub)
kazu = str.count(sub)
joi = str+sub




print(head)if head >0 else print('no object')

print(str,'****',sub,'****',head,'****',kazu,'****',joi)