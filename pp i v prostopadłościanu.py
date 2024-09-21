import math

print(math.sqrt(9))
print(math.pi)

inp = input()
if 'a' == inp:
    print('pp - a v -b')
    inp = input('co liczę =')
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if inp == 'a':
        print(2*a*b+2*a*c+2*b*c)
    elif inp == 'b':
        print(a*b*c)