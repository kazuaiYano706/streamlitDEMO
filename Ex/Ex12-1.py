try:
    a = int(input("int:"))
    b = int(input('int:'))

    print(a*b)
    print(a/b)

except ValueError:
    print('Value Error')
except ZeroDivisionError:
    print('Zero /')
else:
    print('OK')
finally:
    print('you are finish.')

