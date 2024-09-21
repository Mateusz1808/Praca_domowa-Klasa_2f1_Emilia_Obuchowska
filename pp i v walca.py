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
    if inp == 'a':
        print(2*Pi*r**2+2*Pi*r*h)
    elif inp == 'b':
        print(Pi*r**2*h)