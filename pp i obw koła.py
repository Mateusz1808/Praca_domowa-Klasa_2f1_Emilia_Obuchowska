import math 

print(math.sqrt(9))
Pi = math.pi

inp = input()
if 'a' == inp:
    print('pp - a obw - b')
    inp = input('co liczę =')
    r = float(input('r = '))
    if inp == 'a':
        print(Pi*(r**2))
    elif inp == 'b':
        print(2*Pi*r)