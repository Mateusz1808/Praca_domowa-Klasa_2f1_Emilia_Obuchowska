import math

print(math.sqrt(9))
print(math.pi)

inp = input()
if 'a' == inp:
    print('pp - a obw - b')
    inp = input('co liczę =')
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    d = float(input('d = '))
    h = float(input('h = '))
    if inp == 'a':
        print((a+b)*h/2)
    elif inp == 'b':
        print(a+b+c+d)