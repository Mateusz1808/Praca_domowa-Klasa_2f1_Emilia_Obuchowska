import math 

print(math.sqrt(9))
print(math.pi)

inp = input()
if 'a' == inp:
    print('pp - a obw - b')
    inp = input('co liczę =')
    a = float(input('a = '))
    b = float(input('b = '))
    h = float(input('h = '))
    if inp == 'a':
        print(a*h)
    elif inp == 'b':
        print(2*a+2*b)