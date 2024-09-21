import math

print(math.sqrt(9))
print(math.pi)

inp = input()
if 'a' == inp:
    print('pp - a obw - b')
    inp = input('co liczę =')
    a = float(input('a = '))
    b = float(input('b = '))
    if inp == 'a':
        print(a*b)
    elif inp == 'b':
        print(2*a+2*b)