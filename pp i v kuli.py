import math

print(math.sqrt(9))
print(math.pi)
Pi = math.pi

inp = input()
if 'a' == inp:
    print('pp - a v -b')
    inp = input('co liczę =')
    r = float(input('r = '))
    if inp == 'a':
        print(4*Pi*r**2)
    elif inp == 'b':
        print(4/3*Pi*r**3)