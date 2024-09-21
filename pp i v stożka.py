import math

print(math.sqrt(9))
print(math.pi)
Pi = math.pi 

inp = input()
if 'a' == inp:
    print('pp - a v -b')
    inp = input('co liczę =')
    r = float(input('r = '))
    h = float(input('h = '))
    l = float(input('l = '))
    if inp == 'a':
        print(Pi*r**2+Pi*r*l)
    elif inp == 'b':
        print(1/3*Pi*r**2*h)